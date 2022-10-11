from rest_framework import serializers
from apps.users.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance, validated_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username':  instance['username'],
            'email':  instance['email'],
            'password': instance['password']
        }


# class TestUserSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 200)
#     email = serializers.EmailField()

#     def validate_name(self,value):
#         #custom validations
#         if 'develop' in value:
#             raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
#         return value
    
#     def validate_email(self,value):
#         if value == '':
#             raise serializers.ValidationError('Tiene que indicar un correo')

#         # if self.validate_name(self.context['name']) in value:
#         #     raise serializers.ValidationError('El email no puede contener el nombre')
#         return value

#     def validate(self,data):
#         return(data)

#     def create(self, validated_data):
#         return self.model.objects.create(**validated_data)

#     def update(self,instance,validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.email = validate_data.get('email', instance.email)
#         instance.save()
#         return instance

    # ejemplo save() es el mismo save del modelo. no el del serializador
    # def save(self):
    #     print(self)