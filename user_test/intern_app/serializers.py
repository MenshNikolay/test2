from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string


from intern_app.models import RefToken

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email','password']

    def uniq_email_validation(self, email):
        if User.objects.filter(email=email).exists():
            raise  serializers.ValidationError("We've seen this email. Try another or login.")
        return email
        

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        self.uniq_email_validation(email)

        username = 'user' + get_random_string(length=6, allowed_chars='0123456789')
        
        return self.Meta.model.objects.create_user(username=username, email=email, password=password)
    
class RefTokenSerializer(serializers.ModelSerializer):
       class Meta:
        model = RefToken
        fields = ['ref_token']