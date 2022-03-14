from interview.models import Participant, Interview
from django.db.models import Q
from datetime import datetime

def getAllParticipant():
    return list(Participant.objects.all())

def getOverlappingParticipants(participant_id, interview, exlude_id=None):
    return Interview.objects.filter(
        Q(
            participants__id = participant_id,
            start_time__gte = interview['start_time'],
            start_time__lte = interview['end_time']) |
        Q(
            participants__id = participant_id,
            end_time__gte = interview['start_time'],
            end_time__lte = interview['end_time']
        )
    ).exclude(id=exlude_id)

def getParticipantsFullName(overlap):
    return list(map(
        lambda _participant: _participant.first_name + " " + _participant.last_name, 
        Participant.objects.filter(id__in=overlap)
    ))

def getUpcomingInterviews():
    today_now = datetime.now()

    return list(Interview.objects.filter(
        start_time__gte = today_now
    ))

def getEmailsFromParticipantId(pariticipants_id):
    return list(map(
        lambda _participant: _participant.email,
        Participant.objects.filter(id__in=pariticipants_id)
    ))

def getUrlFromParticipantId(participant_id):
    return Participant.objects.get(id=participant_id).resume