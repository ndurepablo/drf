from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    
    # custom validation
    def validate_name(self, value):
        if 'develop' in value:
            # error asignado al campo 'name': type error -> 'name'
            raise serializers.ValidationError('Error, no puede existir un usuario con ese nombre')
        return value
    #2
    def validate_email(self, value):
        if value == '':
            # error asignado al campo 'email': type error -> 'email'
            raise serializers.ValidationError('Tiene que indicar un correo')
        
        # accedemos al return value de validate name y enviamos el context name
        # validate_name -> {name: pablo}; context -> {name: pablo}
        # por lo que: validate_name('pablo') es lo mismo que validate_name(context['name'])
        if self.validate_name(self.context['name']) in value:
            # error asignado al campo 'email': type error -> 'email'
            raise serializers.ValidationError('El mail no puede contener el nombre')
        return value
    #3
    def validate(self, data):
        # error no asignado a un campo: non_field_error
        if self.data['name'] in data['email']:
            raise serializers.ValidationError('El mail no puede contener el nombre')
        return data