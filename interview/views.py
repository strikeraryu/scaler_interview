from django.shortcuts import render, redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from .helpers.utils import isValid
from .helpers.queries import getAllParticipant, getUpcomingInterviews, getEmailsFromParticipantId, getUrlFromParticipantId
from .helpers.mutations import insertInterview, updateInterview, updateParticipantUrl
from scaler_interview.settings import MEDIA_ROOT

def createInterview(request):
    context = {}

    if request.method == 'POST':
        # create interview map from POST request
        interview = {
            'title': request.POST.get('title'),
            'start_time': request.POST.get('start_time'),
            'end_time': request.POST.get('end_time'),
            'participants': request.POST.getlist('participants')
        }
        # check is data valid
        is_valid, context['error'] = isValid(interview)


        if is_valid:
            try:
                insertInterview(interview)
                emails = getEmailsFromParticipantId(interview['participants'])
                send_mail(
                    f'Interview Schedule - {interview["title"]}',
                    f'Hi,\nYou have a Interview Schedule - {interview["title"]} from {interview["start_time"]} to {interview["end_time"]}\n\nThank You\nInterview.com',
                    'amata.family59@gmail.com',
                    emails,
                    fail_silently=False,
                )
            except Exception as e:
                return HttpResponse(f'''
                    <h1> 
                        Error occured - {e}
                    <h1>
                ''') 


        else:
            context.update({ 
                'title' : interview['title'],
                'start_time' : interview['start_time'],
                'end_time' : interview['end_time'],
                'checked_participants' : interview['participants']
            })
            


    # get all participants
    context['participants'] = getAllParticipant()
    return render(request, 'create.html', context)


def showInterviews(request, edit_id=None):
    context = {}
    if request.method == "POST":
        # create interview map from POST request
        interview = {
            'title': request.POST.get('title'),
            'start_time': request.POST.get('start_time'),
            'end_time': request.POST.get('end_time'),
            'participants': request.POST.getlist('participants')
        }
        # check is data valid
        is_valid, context['error'] = isValid(interview, edit_id)


        if is_valid:
            try:
                updateInterview(edit_id, interview)
            except Exception as e:
                return HttpResponse(f'''
                    <h1> 
                        Error occured - {e}
                    <h1>
                ''')

            return redirect('/interviews')

    context['interviews'] = getUpcomingInterviews()
    context['edit_id'] = edit_id

    if edit_id:
        context['participants'] = getAllParticipant()

    return render(request, 'list.html', context)


def uploadResume(request, upload_id=None):
    context = {}
    if request.method == 'POST' and request.FILES['resume'] :
        resume = request.FILES['resume']
        fs = FileSystemStorage()
        participant_path_url = getUrlFromParticipantId(upload_id)
        try:
            if participant_path_url:
                fs.delete(participant_path_url)
            filename = fs.save(resume.name, resume)
            uploaded_file_url = fs.url(filename)
            updateParticipantUrl(filename, upload_id)
            return redirect('/upload')
        except Exception as e:
            return HttpResponse(f'''
                <h1> 
                    Error occured - {e}
                <h1>
            ''')

    context['participants'] = getAllParticipant()
    return render(request, 'upload.html', context)