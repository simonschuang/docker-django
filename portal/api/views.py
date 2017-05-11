from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Instance
from api.serializers import InstanceSerializer


@csrf_exempt
def instance_list(request):
    """
    List all code instances, or create a new instance.
    """
    if request.method == 'GET':
        instances = Instance.objects.all()
        serializer = InstanceSerializer(instances, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InstanceSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def instance_detail(request, pk):
    """
    Retrieve, update or delete a code instance.
    """
    try:
        instance = Instance.objects.get(pk=pk)
    except Instance.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = InstanceSerializer(instance)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InstanceSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)
