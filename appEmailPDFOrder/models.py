from django.db import models

class Clientes(models.Model):

    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    cnpj = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )

    representante = models.CharField(
        max_length=100,
        default="None"
    )


class Produtos(models.Model):

    nome = models.CharField(
        max_length = 100,
        null = False,
        blank = False
    )

    tamanho = models.PositiveSmallIntegerField(
        default=0,
        null = False,
        blank= False
    )

    cor = models.CharField(
        max_length = 30,
        null= False,
        blank= False
    )

    preco = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2
    )

class Pedidos(models.Model):

    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    data = models.DateTimeField(auto_now_add=True)


class Itens(models.Model):

    pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)

    quantidade = models.PositiveBigIntegerField(
        max_length= 4,
        null= False,
        blank= False
    )

