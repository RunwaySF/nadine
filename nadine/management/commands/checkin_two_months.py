from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

from django.utils.timezone import localtime, now
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from nadine.models.membership import Membership
from nadine import email


class Command(BaseCommand):
    help = "Check-in with users after two months"

    def handle(*args, **options):
        # Pull the memberships that started 2 months ago and send a survey
        # if they are still active and this was their first membership
        today = localtime(now()).date()
        two_months_ago = today - relativedelta(months=2)
        for membership in Membership.objects.filter(start_date=two_months_ago):
            if Membership.objects.filter(user=membership.user, start_date__lt=two_months_ago).count() == 0:
                if membership.user.profile.is_active():
                    email.send_member_survey(membership.user)


# Copyright 2017 Office Nomads LLC (http://officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
