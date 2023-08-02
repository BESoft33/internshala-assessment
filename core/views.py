from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Invoice, InvoiceDetails
from .serializers import InvoiceSerializer, InvoiceDetailsSerializer


class InvoiceView(APIView):
    def get(self, request):
        invoice = Invoice.objects.all()
        serializer = InvoiceSerializer(invoice, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class InvoiceItemView(APIView):
    def get(self, request, pk):
        invoice = get_object_or_404(Invoice, id=pk)
        if invoice:
            serializer = InvoiceSerializer(invoice)
            return Response(serializer.data)

        return status.HTTP_404_NOT_FOUND




class InvoiceItemDetailsView(APIView):
    def get(self, request, pk):
        details = get_object_or_404(InvoiceDetails, id=pk)
        if details:
            serializer = InvoiceDetailsSerializer(details)
            return Response(serializer.data)

        return status.HTTP_404_NOT_FOUND




class InvoiceDetailsView(APIView):
    def get(self, request):
        invoice_details = InvoiceDetails.objects.all()
        serializer = InvoiceDetailsSerializer(invoice_details, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InvoiceDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

