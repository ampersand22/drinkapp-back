from rest_framework import serializers
from .models import FriendRequest, UserAccount, Profile

### ALLOWS YOU TO CREATE AND CHECK PASSWORDS
from django.contrib.auth.hashers import make_password, check_password

# ReadOnlyField class is always read-only, and will be used for serialized representations, but will not be 
# used for updating model instances when they are deserialized. We could have also 
# used CharField(read_only=True) here.
owner = serializers.ReadOnlyField(source='owner.username')


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'email', 'password')

    ### THIS HASHES A NEW USERS PASSWORD WHEN THEY CREATE AN ACCOUNT
    def create(self, validated_data):
        user = UserAccount.objects.create(
        email=validated_data['email'],
        password = make_password(validated_data['password'])
        )
        user.save()
        return user

    ### THIS MAKES SURE THEIR UPDATED PASSWORDS ARE ALSO HASHED
    def update(self,instance, validated_data):
        user = UserAccount.objects.get(email=validated_data["email"])
        user.password = make_password(validated_data["password"])
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'owner', 'user', 'image', 'bio', 'friends')
        
class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ('id', 'to_user', 'from_user', 'timestamp' )