import django_filters

from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from ingredients.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node,)


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        interfaces = (relay.Node,)
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact']
        }


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr=['icontains'])

    class Meta:
        model = Category
        fields = ['name', 'ingredients']

    # Para filtrar por el usuario logeado.
    # @property
    # def qs(self):
    #     return super(CategoryFilter, self).qs.filter(owner=self.request.user)


class Query:
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode, filterset_class=CategoryFilter)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
