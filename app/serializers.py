from rest_framework import serializers

from app.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "nation",
            "currency",
            "value",
            "unit",
            "issueyear",
            "circability",
            "dissolved",
            "count",
            "collection",
            "imgF",
            "imgB",
            "notes",
            "timestamp",
            "updated",
        )
        model = Currency
