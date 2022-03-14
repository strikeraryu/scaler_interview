from interview.models import Interview, Participant

def insertInterview(interview):
    # insert interview
    _interview = Interview.objects.create(
        title = interview['title'],
        start_time = interview['start_time'],
        end_time = interview['end_time']
    )

    # insert participants in the interview
    for participant_id in interview['participants']:
        participant = Participant.objects.get(id = participant_id)
        _interview.participants.add(participant)
    
    _interview.save()

def updateInterview(interview_id, interview):
    # update interview
    _interview = Interview.objects.get(id=interview_id)
    _interview.title = interview['title']
    _interview.start_time = interview['start_time']
    _interview.end_time = interview['end_time']
    _interview.participants.clear()
    

    # update participants in the interview
    for participant_id in interview['participants']:
        participant = Participant.objects.get(id = participant_id)
        _interview.participants.add(participant)
    
    _interview.save()

def updateParticipantUrl(url, participant_id):
    _participant = Participant.objects.get(id = participant_id)
    _participant.resume = url

    _participant.save()