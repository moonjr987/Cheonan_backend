from rest_framework import serializers
from app.models import MyUser
from django.core.validators import RegexValidator
from .models import CultureBank

class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        validators=[
            RegexValidator(
                r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()_+])[A-Za-z\d~!@#$%^&*()_+]{8,}$',
                message='비밀번호는 대문자, 소문자, 숫자, 특수문자를 최소 하나씩 포함해야 합니다.',
                code='invalid_password'
            )
        ]
    )
    userid = serializers.RegexField(
        r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]+$', 
        required=True,
        error_messages={
            'invalid': '영문과 숫자가 반드시 포함되어야 합니다.'
        }
    )
    email = serializers.EmailField(required=True)
    
    username = serializers.CharField(
        max_length=150,
        required=True,
        min_length=2,
        error_messages={
            'min_length': '최소 2글자 이상 입력해주세요.'
        }
    )


    def create(self, validated_data):
        user = MyUser.objects.create(
        userid=validated_data['userid'],
        username=validated_data['username'],
        email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = MyUser
        fields = ( 'email', 'password', 'username', 'userid')


class CultureBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureBank
        fields = '__all__'