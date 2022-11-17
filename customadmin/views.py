from django.http import HttpResponse
from django.shortcuts import render
from api.models import *
from django.views import View


class AdminIndex(View):
    template_name = "AdminPage/index.html"

    def get(self, request):
        contents = ContentTemplate.objects.all()
        numbers = NumberGroup.objects.all()
        groups = Group.objects.all()
        args = {
            "contents": contents,
            "numbers": numbers,
            "groups": groups
        }
        return render(request, self.template_name, args)

    def post(self, request):
        content = request.POST.get("content")
        number = request.POST.get("number")
        groups = request.POST.get("group")
        if request.method == "POST":
            message = SendMessageModel(
                content=ContentTemplate.objects.get(id=content),
                number=NumberGroup.objects.get(id=number),
                group=Group.objects.get(id=groups)
            )
            message.save()
            for n in message.group.customers.all():
                account_sid = "AC2b0cc7c783ccc1e82f3771636dda5e73"
                auth_token = "97a616e1b312b9b4ea0e74c27099377e"
                client = Client(
                        account_sid, auth_token
                    )

                send_message = client.messages.create(
                                body=message.content.title,
                                from_=f"+{message.number.number}",
                                to=n.phone_number,
                                # to="+8801610968643"
                            )
                n.is_sent = True
                print(str(n.phone_number))
                n.save()

            return HttpResponse("All Sent")





