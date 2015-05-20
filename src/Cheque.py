#!/usr/bin/python
# -*- coding: utf-8 -*-

from decimal import Decimal

class Cheque:
    
    _numbers = {
        1 : "um",
        2 : "dois",
        3 : "tres",
        4 : "quatro",
        5 : "cinco",
        6 : "seis",
        7 : "sete",
        8 : "oito",
        9 : "nove",
        10 : "dez",
        11 : "onze",
        12 : "doze",
        13 : "treze",
        14 : "quatorze",
        15 : "quinze",
        16 : "dezesseis",
        17 : "dezessete",
        18 : "dezoito",
        19 : "dezenove",
        20 : "vinte",
        30 : "trinta",
        40 : "quarenta",
        50 : "cinquenta",
        60 : "sessenta",
        70 : "setenta",
        80 : "oitenta",
        90 : "noventa",
        100 : "cento",
        200 : "duzentos",
        300 : "trezentos",
        400 : "quatrocentos",
        500 : "quinhentos",
        600 : "seicentos",
        700 : "setecentos",
        800 : "oitocentos",
        900 : "novecentos"
	}
    
    def __init__(self, valor):
        self.valor = valor
        
    def humanize(self):
        parteInteira = int(self.valor)
        reais = (self.convertToExtensive(parteInteira) + (" reais" if parteInteira != 1 else " real")) if(parteInteira > 0) else ""
        
        parteFracionaria = (Decimal(str(self.valor)) % 1) * 100
        centavos = " e " + self.convertToExtensive(int(parteFracionaria)) + " centavos" if (parteFracionaria > 0) else ""
        
        return reais + centavos


    def convertToExtensive(self, valorEntrada):
        tamanho = len(str(valorEntrada))
        
        if tamanho <= 2:
          return self.humanizedDezena(valorEntrada)
        
        if tamanho == 3:
          return self.humanizedCentena(valorEntrada)
        
        if tamanho >= 4:
            parteMilhar = valorEntrada / 1000
            parteCentena = valorEntrada % 1000
            humanizedMilhar = (self.convertToExtensive(parteMilhar) + " mil") if parteMilhar != 1 else "mil"
            
            if parteCentena > 0:
                return humanizedMilhar + ", " + self.humanizedCentena(parteCentena)
            else:
                return humanizedMilhar


    def humanizedDezena(self, valor):
        if (valor <= 20 or (valor % 10) == 0):
            return Cheque._numbers[valor]
        else:
            parteDezena = valor - (valor % 10)
            parteUnidade = valor % 10
            humanizedDezena = Cheque._numbers[parteDezena]
            humanizedUnidade = Cheque._numbers[parteUnidade]
            return humanizedDezena + " e " + humanizedUnidade



    def humanizedCentena(self, valor):
        parteDezena = valor % 100
        parteCentena = valor - parteDezena
        if (valor == 100 and parteDezena == 0):
            return "cem"
        else:
            return Cheque._numbers[parteCentena] + " e " + self.humanizedDezena(parteDezena)
    
    
