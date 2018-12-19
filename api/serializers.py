from rest_framework import serializers
from restaurants.models import Restaurant
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class RestaurantListSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()

    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )

    owner = UserSerializer()

    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )

    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )

    class Meta:
        model = Restaurant
        fields = [
            'name',
            'opening_time',
            'closing_time',
            'owner',
            'detail',
            'update',
            'delete',
            'created_by',
            'updated_by',
            'deleted_by'
            ]

    def get_created_by(self, obj):
        return " The owner is: %s %s." % (obj.owner.first_name, obj.owner.last_name)

    def get_updated_by(self, obj):
        return " The fields were updated by: %s %s." % (obj.owner.first_name, obj.owner.last_name)

    def get_deleted_by(self, obj):
        return " The fields were deleted by: %s %s." % (obj.owner.first_name, obj.owner.last_name)



class RestaurantDetailSerializer(serializers.ModelSerializer):
    updated_by = serializers.SerializerMethodField()
    deleted_by = serializers.SerializerMethodField()

    update = serializers.HyperlinkedIdentityField(
        view_name = "api-update",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )

    delete = serializers.HyperlinkedIdentityField(
        view_name = "api-delete",
        lookup_field = "id",
        lookup_url_kwarg = "restaurant_id"
        )


    class Meta:
        model = Restaurant
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'opening_time',
            'closing_time',
            'updated_by',
            'deleted_by',
            'update',
            'delete'
            ]

    def get_updated_by(self, obj):
        return " The fields were updated by: %s %s." % (obj.owner.first_name, obj.owner.last_name)

    def get_deleted_by(self, obj):
        return " The fields were deleted by: %s %s." % (obj.owner.first_name, obj.owner.last_name)


class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'description',
            'opening_time',
            'closing_time',
            ]