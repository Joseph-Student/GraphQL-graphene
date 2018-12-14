import graphene

from graphene_django.types import DjangoObjectType
from ingredients.models import Category, Ingredient
from ingredients.mutations import CategoryMutation, IngredientMutation


# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = Category
#
#
# class IngredientType(DjangoObjectType):
#     class Meta:
#         model = Ingredient


class Query:
    category = graphene.Field(CategoryMutation, id=graphene.Int(), name=graphene.String())
    all_categories = graphene.List(CategoryMutation)

    ingredient = graphene.Field(IngredientMutation, id=graphene.Int(), name=graphene.String())
    all_ingredients = graphene.List(IngredientMutation)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)
        return None

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_ingredient(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredient.objects.get(pk=id)

        if name is not None:
            return Ingredient.objects.get(name=name)
        return None
