from .constants import participantsLimit
from .queries import getOverlappingParticipants, getParticipantsFullName

def isValid(interview, exclude_id=None):
    # check if start time and end time is valid
    if interview['start_time'] >= interview['end_time']:
        return False, 'Please enter valid time interval'

    # check if number of participants is greater than the limit
    if len(interview['participants']) < participantsLimit:
        return False, 'Add 2 or More participants'

    # check if no overlapping interval for any participants
    overlap_ids = []

    for participant_id in interview['participants']:
        interviews = getOverlappingParticipants(participant_id, interview, exclude_id)

        if len(interviews) > 0:
            overlap_ids.append(participant_id)

    
    if len(overlap_ids) > 0:
        overlap_names = getParticipantsFullName(overlap_ids)
        error = 'No free slot for ' + ", ".join(overlap_names)
        return False, error

    return True, ''
    