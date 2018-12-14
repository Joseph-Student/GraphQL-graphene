from rest_framework import serializers
from ingredients.models import Category, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    # ingredients = IngredientSerializer()

    class Meta:
        model = Category
        fields = '__all__'
