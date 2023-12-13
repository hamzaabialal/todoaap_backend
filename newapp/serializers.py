from rest_framework import serializers
from .models import ToDoModel


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoModel
        fields = '__all__'

    def validate_title(self, value):
        # Email validation
        if "@" in value or "." in value:
            if "@" not in value or "." not in value:
                raise serializers.ValidationError(
                    "Enter a valid email address.")
            # Username validation
        elif '.' in value:
            raise serializers.ValidationError(
                "Name should not contain a dot (.)")
            # Length validation
        elif len(value) < 5 and len(value) > 30:
            raise serializers.ValidationError("Title must be at least 30 characters long.")
            # Alphabetic characters check
        elif value.replace(" ", "").islower():
            raise serializers.ValidationError(
                "Name should only contain letters.")

        return value