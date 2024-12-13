from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from treyler.models.treyler import Treyler
from api.serializers.serializers.serializers import TreylerSerializers
from rest_framework.response import Response


class TreylerDetail(generics.RetrieveAPIView):
    queryset = Treyler.objects.all()
    serializer_class = TreylerSerializers
    lookup_field = 'title'

    def get(self, request, *args, **kwargs):
        title = kwargs.get('title')
        treyler = get_object_or_404(Treyler, title=title)
        data = {
            "title": treyler.title,
            "description": treyler.description,
            'code': treyler.code,
        }
        if treyler.treyler_id:
            data["treyler_id"] = treyler.treyler_id
        else:
            data["treyler_id"] = request.build_absolute_uri(treyler.treyler_id)
        return Response(data)
