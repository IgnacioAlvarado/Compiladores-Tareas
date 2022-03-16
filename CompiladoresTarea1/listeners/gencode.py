import queue
from antlr.marzoListener import marzoListener
from antlr.marzoParser import marzoParser

class GenCode(marzoListener):
    def __init__(self):
        self.count = 0
        self.valores = []
        self.variables = []
        self.doIf = []
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")
    
    #Números y Variables
    def exitPrimaria(self, ctx:marzoParser.PrimariaContext):
        self.valores.append(ctx.Numero().getText())
    
    def exitLetras(self, ctx:marzoParser.LetrasContext):
        self.variables.append(ctx.Variable().getText())

    #Aritmetica
    def exitSuma(self, ctx:marzoParser.SumaContext):
        self.count+=1
        print("ADD $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
    
    def exitResta(self, ctx:marzoParser.RestaContext):
        self.count+=1
        print("SUB $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))

    def exitDivision(self, ctx:marzoParser.DivisionContext):
        self.count+=1
        print("DIV $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
    
    def exitMultiplicacion(self, ctx:marzoParser.MultiplicacionContext):
        self.count+=1
        print("MULT $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
    
    #Asignación y declaración
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        self.count+=1
        if len(self.doIf) != 0:
            print(str(self.doIf.pop(0)))
        print("li $v"+str(self.count)+", " + str(self.valores.pop(0)))
        self.variables.pop(0)
    
    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        if len(self.doIf) != 0:
            print(str(self.doIf.pop(0)))
        print(str(self.variables.pop(0))+": .int")
    
    #Comparaciones
    def exitGreater(self, ctx:marzoParser.GreaterContext):
        if len(self.doIf) == 0:
            self.count+=1
            print("SGT $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
        else:
            print("BGT "+ str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)+", DO"))
            print("j ELSE")
    
    def exitSmaller(self, ctx:marzoParser.SmallerContext):
        if len(self.doIf) == 0:
            self.count+=1
            print("SLT $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
        else:
            print("BLT "+ str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)+", DO"))
            print("j ELSE")
    
    def exitGreatereq(self, ctx:marzoParser.GreatereqContext):
        if len(self.doIf) == 0:
            self.count+=1
            print("SGE $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
        else:
            print("BGE "+ str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)+", DO"))
            print("j ELSE")
    
    def exitSmallereq(self, ctx:marzoParser.SmallereqContext):
        if len(self.doIf) == 0:
            self.count+=1
            print("SLE $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
        else:
            print("BLE "+ str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)+", DO"))
            print("j ELSE")
    
    def exitEquals(self, ctx:marzoParser.EqualsContext):
        if len(self.doIf) == 0:
            self.count+=1
            print("SEQ $v"+str(self.count)+", " + str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)))
        else:
            print("BEQ "+ str(self.valores.pop(0)) + " ,"+str(self.valores.pop(0)+", DO"))
            print("j ELSE")
    
    #Imprimir
    def exitPrint(self, ctx:marzoParser.PrintContext):
        self.count+=1
        if len(self.doIf) != 0:
            print(str(self.doIf.pop(0)))
        print("li$v"+str(self.count)+","+str(self.valores.pop(0)))
        print("la$a0,$v"+str(self.count))
        print("syscall")
    
    #If
    def enterIf(self, ctx:marzoParser.IfContext):
        self.doIf.append("DO:")
        self.doIf.append("ELSE:")
    


    
