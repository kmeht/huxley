# Copyright (c) 2011-2015 Berkeley Model United Nations. All rights reserved.
# Use of this source code is governed by a BSD License (see LICENSE).
import json

from django.urls import reverse
from django.shortcuts import redirect, render
from django.template import RequestContext

from huxley.api.serializers import UserSerializer
from huxley.core.constants import ContactGender, ContactType, ProgramTypes
from huxley.core.models import Conference


def index(request):
    if request.user.is_superuser:
        return redirect(reverse('admin:index'))

    user_dict = {}
    if request.user.is_authenticated:
        user_dict = UserSerializer(request.user).data

    conference = Conference.get_current()

    conference_dict = {
        'session': conference.session,
        'start_date': {
            'month': conference.start_date.strftime('%B'),
            'day': conference.start_date.strftime('%d'),
            'year': conference.start_date.strftime('%Y')
        },
        'end_date': {
            'month': conference.end_date.strftime('%B'),
            'day': conference.end_date.strftime('%d'),
            'year': conference.end_date.strftime('%Y')
        },
        'early_paper_deadline': {
            'month': conference.early_paper_deadline.strftime('%B'),
            'day': conference.early_paper_deadline.strftime('%d')
        },
        'paper_deadline': {
            'month': conference.paper_deadline.strftime('%B'),
            'day': conference.paper_deadline.strftime('%d')
        },
        'waiver_avail_date': {
            'month': conference.waiver_avail_date.strftime('%m'),
            'day': conference.waiver_avail_date.strftime('%d')
        },
        'waiver_deadline': {
            'month': conference.waiver_deadline.strftime('%m'),
            'day': conference.waiver_deadline.strftime('%d')
        },
        'waiver_link': conference.waiver_link,
        'external': conference.external,
        'treasurer': conference.treasurer,
        'registration_fee': int(conference.registration_fee),
        'delegate_fee': int(conference.delegate_fee),
        'registration_open': conference.open_reg,
        'registration_waitlist': conference.waitlist_reg,
        'position_papers_accepted': conference.position_papers_accepted,
    }

    context = {
        'user_json': json.dumps(user_dict).replace('</', '<\\/'),
        'conference_json': json.dumps(conference_dict),
        'gender_constants': ContactGender.to_json(),
        'contact_types': ContactType.to_json(),
        'program_types': ProgramTypes.to_json(),
    }

    return render(request, 'www.html', context)
