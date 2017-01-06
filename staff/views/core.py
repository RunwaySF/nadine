import os
import traceback
import operator

from datetime import date, datetime, timedelta

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib import messages
from django.conf import settings

from nadine.models.membership import Membership, MembershipPlan, MemberGroups, SecurityDeposit
from nadine.forms import MemberSearchForm, MembershipForm, EventForm
from nadine.utils import network


@staff_member_required
def view_ip(request):
    ip = network.get_addr(request)
    return render(request, 'staff/view_ip.html', {'ip': ip})


@staff_member_required
def view_config(request):
    return render(request, 'staff/view_config.html', {})


@staff_member_required
# TODO - evaluate
def create_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return HttpResponseRedirect(reverse('staff_todo'))
    else:
        event_form = EventForm()
    return render(request, 'staff/create_event.html', {'event_form': event_form})


# Copyright 2017 Office Nomads LLC (http://www.officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
