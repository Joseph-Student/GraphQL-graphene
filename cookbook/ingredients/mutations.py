from django import http
from graphene_django.rest_framework.mutation import SerializerMutation
from ingredients.serializers import CategorySerializer, IngredientSerializer
from ingredients.models import Category


class CategoryMutation(SerializerMutation):
    class Meta:
        serializer_class = CategorySerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'

    # Sobreescribir el metodo update
    # @classmethod
    # def get_serializer_kwargs(cls, root, info, **input):
    #     if 'id' in input:
    #         instance = Category.objects.filter(id=input['id'], owner=info.context.user).first()
    #         if instance:
    #             return {'instance': instance, 'data': input, 'partial': True}
    #         else:
    #             raise http.Http404
    #     return {'data': input, 'partial': True}


class IngredientMutation(SerializerMutation):
    class Meta:
        serializer_class = IngredientSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'
