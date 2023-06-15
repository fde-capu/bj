# fde-capu
# run: sudo apt-install python3-ipython

cacife=100
pingo_inicial=10
dealer_name_f = "Shanna"
dealer_name_m = "Paul"
dealer_name = ""
dealer_money = 100
dealer_gender = "f"
dealer_greed = 0
debug = False
dealer_clothes_f = [
    [   ("seu colar","deixa à mostra seu esbelto pescoço"),
        ("seus óculos","revela o brilho em seu ermo olhar"),
        ("suas luvas","exibe suas mãos esguias"),
        ("seus brincos","exibe suas perfeitas orelhas"),
        "sem mais nenhum acessório para remover"                ],
    [   ("sua gravata","conota um certo ar de embarasso"),
        ("seu paletó","e diz: 'Não se pode ganhar sempre'"),
        ("sua camisa","deixa à mostra seu sutiã bordado"),
        ("seu sutiã","exibe seus majestosos seios"),
        "nua da cintura para cima"                ],
    [   ("seu cinto","e dá uma indignada chicoteada no chão'"),
        ("seus sapatos","move seus dedinhos do pé confortavelmente"),
        ("suas calças","suas roliças e sedosas pernas exibem apenas uma meia-calça semitransparente"),
        ("sua meia-calça","sua calcinha bordada parece muito delicada"),
        ("sua calcinha","uma atmosfera sensual toma conta da mesa"),
        "perfeitamente nua da cintura para baixo"               ],
    "completamente nua, e ela é linda!" ]
dealer_clothes_m = [
    [   ("seu relógio","seus punhos são espessos"),
        ("seus óculos","revela o um olhar despreocupado"),
        "sem mais nenhum acessório para remover"                ],
    [   ("sua gravata","conota um certo ar de embarasso"),
        ("seu paletó","e seu perfume invade a sala"),
        ("sua camisa","deixa à mostra seu forte peitoral e sua barriga de tanquinho"),
        "nu da cintura para cima"                ],
    [   ("seu cinto","dizendo: 'Lá se vai algo que poderia ser usado de outra forma!'"),
        ("seus sapatos","move seus dedos do pé agitadamente"),
        ("suas calças","suas bem definidas e roliças pernas"),
        ("sua cueca","uma atmosfera sensual toma conta da mesa"),
        "perfeitamente nu da cintura para baixo"               ],
    "completamente nu, e ele é másculo!" ]
dealer_clothes=[]


import random
from IPython.display import clear_output
import os
import math

class zz():
    def written(self,m_f):
        written_num=["zero",("um","uma"),("dois","duas"),"três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezesete","dezoito","dezenove","vinte"]
        if (int(self)) > 20:return str(self)
        if type(written_num[int(self)]) == tuple:
            if m_f == "f": return written_num[int(self)][1]
            return written_num[int(self)][0]
        return written_num[int(self)]
    def plural(self):
        if int(self) == 1:
            return ""
        else:
            return "s"
    def money(self):
        return "$"+str(self)
    def getInt(q=""):
        while True:
            try:
                r = int(input(q+": "))
                break
            except:
                print ("Expected int.")
        return r
    def ask(str,opt):
        ans='zz'
        while not ans in opt:
            try:
                ans = input(str+' ').lower()[0]
            except:
                ans='zz'
        return ans
    def page():
        input("Enter para continuar...")
    def cls():
        os.system('clear')
        clear_output()
    def sumsbytwo(numb):
        if numb == 0 : return []
        if numb == 1 : return [[numb]]
        li=[]
        x=0
        print ("numb:"+str(numb))
        while x < math.ceil(float(numb)/2):
            x+=1
            y=numb-x
            li.append([x,y])
        print (str(numb)+":"+str(li))
        return li
    def rnd(n_or_int=False,integer_or_m=False,optint=False):
        # rnd()     -> 0.0-1.0;
        # rnd(True) -> 0 or 1
        # rnd(3)    -> 0.0-3.0
        # rnd(3, True)  -> 0-3
        # rnd(3, 7)     -> 3.0-7.0
        # rnd(3, 7, True)   -> 3-7
        if type(n_or_int) == bool:
            if n_or_int == True: return random.randint(0,1)
            return random.uniform(0,1)
        else:
            if type(integer_or_m) == bool:
                if integer_or_m == True: return random.randint(0,n_or_int)
                return random.uniform(0,n_or_int)
            else:
                if integer_or_m < n_or_int: temp = integer_or_m; integer_or_m = n_or_int; n_or_int = temp
                if optinf == True:  return random.randint(n_or_int,integer_or_m)
                return random.uniform(n_or_int,integer_or_m)


# 1: 1
# 2: 1,1
# 3: 1,2
# 4: 1,3 2,2
# 5: 1,4 2,3
# 6: 1,5 2,4 3,3
# 7: 1,6 2,5 3,4

# 1,1,3     2,1,2
# 1,1,1,2   2,1,1,1
# 1,1,1,1,1     2,1,1,1

    def sumsbyn(numb,n):
        if n == 1 : return [[numb]]
        if numb == n : return [[1] * numb]
        lr=[]
        li=zz.sumsbytwo(numb)
        z=0
        while z < len(li):
            while len(li[z]) < n:
                ln = zz.sumsbytwo(li[z].pop())
                li[z]+=ln.pop(0)
                for e in reversed(ln):
                    li.insert(z+1,e)
            z+=1
        return li

    def sumlist(numb):
        l=[]
        n = numb
        while n > 0:
            l += zz.sumsbyn(numb,n)
            n -= 1
        # l=[numb]+zz.sumsbytwo(numb)
        # n = 3
        # while n <= numb:
        #     ll=zz.sumsbyn(numb,n)
        #     l+=ll
        #     n+=1
        return l
def page():
    print ("\n")
    zz.page()
    zz.cls()

class Card(object):
    opened=False
    def __init__(self,face,suit):
        self.face=face
        self.suit=suit
        self.val=self.valcalc()
    def __str__(self):
        return  self.doFace()+self.doSuit()
    def doFace(self):
        if self.opened == False: return "✶✶✶"
        df=self.getFace()
        return '{:>2s} '.format(df)
    def getFace(self):
        if self.face == 1: return "A"
        if self.face == 11: return "J"
        if self.face == 12: return "Q"
        if self.face == 13: return "K"
        return str(self.face)
    def doSuit(self):
        if self.opened == False: return "✶✶✶"
        ds=self.getSuit()
        return '{:>2s} '.format(ds)
    def getSuit(self):
        if self.suit == 1:            return "♦"
        elif self.suit == 2:            return "♣"
        elif self.suit == 3:            return "♥"
        elif self.suit == 4:            return "♠"
    def get(self):
        return ["╔═══╗","║"+self.doFace()+"║","║"+self.doSuit()+"║","╚═══╝"]
    def valcalc(self):
        vc=self.face
        if vc >= 11: vc = 10
        if vc == 1: vc = (1,11)
        return vc
class Deck(object):
    def __init__(self,num_of_decks=1):
        self.num_of_decks=num_of_decks
        self.cardlist=self.getCardList()
        self.shuffle()
    def __str__(self):
        out="|"
        for cd in self.cardlist:
            out+=cd.getFace()+cd.getSuit()+"|"
        return out
    def getCardList(self):
        cl=[]
        for dn in list(range(0,self.num_of_decks)):
            for s in list(range(1,5)):
                for i in list(range(1,14)):
                    cl.append(Card(face=i,suit=s))
        return cl
    def shuffle(self):
        random.shuffle(self.cardlist)
        return
    def removeCard(self,face,suit):
        cdrm=Card(face,suit)
        cdrm.opened=True
        firstidx = -1
        for idx, cd in enumerate(self.cardlist):
            if cd.face == face and cd.suit == suit:
                firstidx = idx
                break
        self.cardlist[idx].opened = True
        self.cardlist.pop(idx)
        return
    def allvals(self):
        vlist=[]
        for cd in self.cardlist:
            vlist.append(cd.val)
        return vlist
    def eachcardchance(self):
        cards_left=self.allvals()
        eachcardchance=[0]*12
        for i in range(1,12):
            if i != 1 and i != 11:
                apear = cards_left.count(i)
            else:
                apear = cards_left.count((1,11))
            eachcardchance[i]=apear/(len(cards_left))
        return eachcardchance
class Hand(list):
    bet=0
    def __str__(self):
        hlist=[]
        allh=""
        for cd in self:
            hlist.append(cd.get())
        for i in list(range(0,len(hlist[0]))):
            ln=''
            for ccard in hlist:
                ln += ccard[i] + ""
            allh+=ln+"\n"
        return allh
    def val_str(self):
        totval=0
        gotace=False
        for cd in self:
            if type(cd.val) == tuple:
                gotace=True
                totval+=cd.val[0]
            else:
                totval+=cd.val
        return str(totval)
    def val_list(self):
        vallist=[0]
        hval=0
        freeval=0
        for cd in self:
            if type(cd.val) == tuple:
                for idx, i in enumerate(vallist):
                    vallist[idx]+=cd.val[0]
                    newlist=[freeval]*len(vallist)
                for idx, j in enumerate(newlist):
                    newlist[idx]+=cd.val[1]
                vallist+=newlist
            else:
                for idx,i in enumerate(vallist):
                    vallist[idx]+=cd.val
                    freeval+=cd.val
        return vallist
    def val(self):
        return str(self.val_list())
    def best(self):
        best=0
        for v in self.val_list():
            if v <=21 and v>best:
                best = v
        return best
    def getCard(self,opened):
        # Dá uma carta ao jogador
        hcard = mesa.deck.cardlist.pop()
        hcard.opened=opened
        self.append(hcard)
        return
    def openAll(self):
        for cd in self:
            cd.opened=True
        return
    def blew(self):
        worse=1000
        for v in self.val_list():
            if v < worse:
                worse = v
        if worse > 21: return True
        return False
    def best_string(self):
        if self.blew() == True: return "Estourou"
        best=self.best()
        if best < 21: return str(best)
        if best == 21: return "Black Jack"
    def winloose_str(self):
        bj=""
        if self.blew() == True: return "Perdeu"
        if self.best() > mesa.dealer.hand[0].best(): return "Ganhou"
        if self.best() == mesa.dealer.hand[0].best(): return "Empatou"
        return "Perdeu"
    def winloose_code(self):
        if self.blew() == True: return 2
        if self.best() > mesa.dealer.hand[0].best(): return 1
        if self.best() == mesa.dealer.hand[0].best(): return 3
        return 2
class Player(object):
    global cacife
    playing = True

    def __init__(self,name):
        self.hand=[Hand()]
        self.name=name
        self.money=cacife
    def statusline(self):
        return  ":: " + self.name + " :: " + zz.money(self.money) + " ::"
    def splitHand(self,hand):
        self.hand.append(Hand())
        self.hand[-1].append(self.hand[hand].pop())
        self.hand[hand].getCard(True)
        self.hand[-1].getCard(True)
        return
    def debt(self, val, choose_another=True, hand_id=0):
        if val<0: val *= -1
        if self.money-val < 0:
            print ("Vai colocar " + zz.money(val) + ".")
            roupasval = self.money
            cacifecount=0
            while roupasval < val:
                roupasval += cacife
                cacifecount+=1
            roupasval -= self.money
            sn=""
            chooseAnotherStr = ""
            if choose_another: chooseAnotherStr = "(n)ão, quero escolher outro valor | "
            while sn == "" or ((sn != "n" or choose_another == False) and sn != "s" and sn != "r"):
                sn = input(self.name + " está sem dinheiro. Deseja acrescer mais "+\
                           zz.money(roupasval)+"?\nSerá necessário remover "+zz.written(cacifecount,"f")+\
                           " peça"+zz.plural(cacifecount)+\
                           " da roupa!\n[ (s)im | "+chooseAnotherStr+"já estou sem (r)oupas! ] :: ")
                if len(sn) > 0: sn = sn[0].lower()
            if sn == "s":
                self.money+=roupasval
                print (self.statusline())
                self.money-=val
                self.hand[hand_id].bet+=val
                print ("Certifique-se que "+self.name+" tenha tirado "+zz.written(cacifecount,"f")+" peça"+\
                       zz.plural(cacifecount)+" de sua roupa.")
                page()
            if sn == "n":
                while self.money-val<0 or val<0:
                    val=zz.getInt("Novo valor")
                self.money-=val
                self.hand[hand_id].bet+=val
            if sn == "r":
                if not choose_another:
                    print ("\n"+self.name + " saiu da mesa, foi fazer outra coisa.")
                    mesa.players = [p for p in mesa.players if p.name != self.name]
                    self.playing = False
                    return False
                else:
                    allin=""
                    while allin != "s" and allin != "n":
                        allin=input("Deseja entrar com all-in? [ (s)im | (n)ão, vou escolher outro valor ]").lower()[0]
                    if allin == "s":
                        val=self.money
                        self.money=0
                    if allin == "n":
                        while self.money-val<0 or val<0:
                            val=zz.getInt("Novo valor")
                        self.money-=val
                        self.hand[hand_id].bet+=val
        else:
            self.money-=val
            self.hand[hand_id].bet+=val
        return val
    def debtasdealer(self, val, choose_another=True, hand_id=0):
        if val<0: val *= -1
        if self.money-val < 0:
            print (self.statusline())
            print ("Não tem " + zz.money(val) + ".")
            allnude=True
            for idx, cl in enumerate(dealer_clothes):
                if idx+1==len(dealer_clothes): continue
                if len(cl) > 1: allnude=False
            if allnude == True:
                print (dealer_name+" está "+dealer_clothes[-1]+"\n\nAgora el"+mesa.dealer_ab()+" pode fazer o que você quiser!")
                return "theend"
            roupasval = self.money
            cacifecount=0
            while roupasval < val:
                roupasval += cacife
                cacifecount+=1
            roupasval -= self.money
            for i in range(0,cacifecount):
                clothgroup=[None]
                while len(clothgroup) == 1:
                    rn = zz.rnd(len(dealer_clothes)-2,True)
                    clothgroup = dealer_clothes[rn]
                item = clothgroup[0][0]
                item_d = clothgroup[0][1]
                dealer_clothes[rn].pop(0)
                print ("El"+mesa.dealer_ab()+" retira "+item+", "+item_d+".")
                self.money += cacife
                if len(dealer_clothes[rn])==1:
                    print ("El"+mesa.dealer_ab()+" está "+dealer_clothes[rn][0]+".\n")
                    allnude=True
                    for idx, cl in enumerate(dealer_clothes):
                        if idx+1==len(dealer_clothes): continue
                        if len(cl) > 1: allnude=False
                    if allnude == True:
                        print (dealer_name+" ficou "+dealer_clothes[-1]+"\n")
                        return "theend"
        self.money-=val
        return val

class BJTable(object):
    global pingo_inicial
    global dealer_name
    global dealer_clothes
    global dealer_gender
    players=[]
    dealer=Player(dealer_name)
    pingo=pingo_inicial
    value=0
    def get(self,pelf,ahand=0):
        out=""
        out += self.dealer.statusline()+"\n"
        if self.dealer.hand[0].best() == 21:
            self.dealer.hand[0].openAll()
        out += str(self.dealer.hand[0])
        if self.dealer.hand[0].best() == 21:
            out += self.dealer.hand[0].best_string()
        out += "\n\n"
        out += pelf.statusline()+"\n"
        if len(pelf.hand) > 1 : out += "\nMão "+str(ahand)+":\n"
        out += str(pelf.hand[ahand])+""
        out += pelf.hand[ahand].val()+"\n\n"
        out += "Aposta: $"+str(pelf.hand[ahand].bet)+".\n"
        return out
    def get_dealer(self):
        out=""
        out += self.dealer.statusline()+"\n"
        self.dealer.hand[0].openAll()
        out += str(self.dealer.hand[0])
        out += self.dealer.hand[0].best_string()
        out += "\n\n"
        for player in mesa.players:
            for idx, han in enumerate(player.hand):
                ifhands = ""
                if len(player.hand)>1:
                    ifhands = "\tMão "+str(idx)
                out += player.name + "" + ifhands + "\t$" + str(han.bet) + "\t[" + han.best_string() + "]\n"
        return out
    def get_results(self):
        out = ""
        out += self.dealer.statusline()+"\t\t["+self.dealer.hand[0].best_string()+"]\n"
        for player in mesa.players:
            for idx, han in enumerate(player.hand):
                ifhands = ""
                if len(player.hand)>1:
                    ifhands = "\tMão "+str(idx)
                winloose = han.winloose_str()
                out += player.statusline() + "" + ifhands + "\t$" + str(han.bet) + "\t[" + han.best_string() + "]\t"+winloose+".\n"
        return out
    def passvalues(self):   # Algo bugado.
        for player in mesa.players:
            for idx, han in enumerate(player.hand):
                winloose = han.winloose_code()
                mao=""
                if len(player.hand) > 1:mao=" (mão "+str(idx)+")"
                if winloose == 1:
                    print (player.name+" ganhou $"+str(han.bet*2)+mao+".")
                    player.money+=han.bet*2
                    # Ver se quebrou a banca
                    if mesa.dealer.debtasdealer(han.bet) == "theend": return "theend"
                if winloose == 2:
                    # print (player.name+" perdeu $"+str(han.bet)+mao+".")
                    mesa.dealer.money+=han.bet
                if winloose == 3:
                    print (player.name+" empatou, $"+str(han.bet)+mao+" devolvidos.")
                    player.money+=han.bet
            print(player.statusline())
        print(mesa.dealer.statusline())
        return
    def dealer_chances(self):
        chance_mintomax=0
        dealer_hand = self.dealer.hand[0].val_list()
        dealer_needs=self.higherPlayerHandVal()
        if dealer_needs < 21: dealer_needs += 1
        for dhv in dealer_hand:
            if dhv > 21: continue
            score_needed=21-dhv
            min_score_needed=dealer_needs-dhv
            if score_needed > 0:
                eachcardchance=self.deck.eachcardchance()
            else:
                return 1 # wins
            for i in range(1,12):
                if i >= min_score_needed and i <= score_needed:
                    chance_mintomax+=eachcardchance[i]
        return chance_mintomax
    def dealer_safe(self):
        chance_safe=0
        dealer_hand = self.dealer.hand[0].val_list()
        dealer_needs=self.higherPlayerHandVal()
        if dealer_needs < 21: dealer_needs += 1
        for dhv in dealer_hand:
            if dhv > 21: continue
            score_needed=21-dhv
            min_score_needed=dealer_needs-dhv
            if score_needed > 0:
                eachcardchance=self.deck.eachcardchance()
            else:
                return 0 # wins
            for i in range(1,12):
                if i <= score_needed:
                    chance_safe+=eachcardchance[i]
        return chance_safe
    def dealer_chances_toblow(self):
        chance_blow=0
        dealer_hand = self.dealer.hand[0].val_list()
        dealer_needs=self.higherPlayerHandVal()
        if dealer_needs < 21: dealer_needs += 1
        for dhv in dealer_hand:
            if dhv > 21: continue
            score_needed=21-dhv
            min_score_needed=dealer_needs-dhv
            if score_needed > 0:
                eachcardchance=self.deck.eachcardchance()
            else:
                return 0 # wins
            for i in range(1,12):
                if i > score_needed:
                    chance_blow+=eachcardchance[i]
        return chance_blow
    def dealer_winrate(self):
        dealer_hand = self.dealer.hand[0].best()
        players_hands = self.playershands()
        wincount=0
        for v in players_hands:
            if v < dealer_hand:
                wincount+=1
        return wincount/len(self.players)
    def dealer_ab(self):
        if self.dealer_gender=="h": return "e"
        return "a"
    def higherPlayerHandVal(self):
        higher=0
        for player in self.players:
            for han in player.hand:
                best = han.best()
                if best > higher: higher = han.best()
        return higher
    def playershands(self):
        hands=[]
        for player in self.players:
            for h in player.hand:
                hands.append(h.best())
        return hands
    def dealer_think(self):
        global dealer_greed
        win_chance = self.dealer_chances()
        safe_chance = self.dealer_safe()
        blow_chance = self.dealer_chances_toblow()
        dealer_win_rate = self.dealer_winrate()
        if self.dealer.hand[0].best == 21:return "passou"
        if safe_chance+dealer_greed>blow_chance:return "chamou"
        if dealer_win_rate == 0:return "chamou"
        return "passou"

mesa=BJTable()
mesa.dealer.money=dealer_money
#♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥
def BlackJack():
    global mesa
    global dealer_name_f
    global dealer_name_m
    global dealer_name
    global dealer_clothes_f
    global dealer_clothes_m
    global dealer_clothes

    print ("\n\n\n\n          ♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥\n          ♠♦    B L A C K   J A C K    ♣♥\n          ♣♥     por Flávio Carrara    ♠♦\n          ♣♥♦♣♥♠♦♣♥♠♦♣♥♠♦♣♥♠ v. 1.0 ♦♣♥♠♦\n\n\n\n")
    while True:
        try:
            n_pl = int(input("Número de jogadores: "))
            break
        except:
            print ("Entrada inválida.")
    while True:
        try:
            mesa.n_decks = int(input("Número de baralhos: "))
            break
        except:
            print ("Entrada inválida.")

    for i in list(range(1,n_pl+1)):
        pl_name = input("Nome player "+str(i)+": ")
        mesa.players.append(Player(pl_name))

    d_gender = ""
    while d_gender != "m" and d_gender != "h":
        d_gender = input("Gênero do dealer [ (m)ulher | (h)omem ]: ")
    if d_gender == "m":
        dealer_name=dealer_name_f
        dealer_clothes=dealer_clothes_f
    else:
        dealer_name=dealer_name_m
        dealer_clothes=dealer_clothes_m
    mesa.dealer.name=dealer_name
    mesa.dealer_gender=d_gender

    ofim=False
    while ofim==False:
        mesa.deck=Deck(mesa.n_decks)
        zz.cls()
        # Para cada jogador:
        for player in mesa.players:
            # Está jogando:
            player.playing = True
            # Retira pingo e já coloca na hand[0]
            print (player.statusline())
            pa=zz.ask("[ (p)ingar ($"+str(mesa.pingo)+") | (a)postar ]","pa")
            if pa == "p" or pa == "":
                a = player.debt(mesa.pingo, False, 0)
                if a:
                    print (player.name + " pingou " + zz.money(a) + ".")
                    print (player.statusline()+"\n")
            if pa == "a":
                v=0
                while v < mesa.pingo:
                    v = zz.getInt("Apostar quanto? (Mínimo: $"+str(mesa.pingo)+")")
                a = player.debt(v, False, 0)
                if a:
                    print (player.name + " apostou " + zz.money(a) + ".")
                    print (player.statusline()+"\n")
            page()
        if len(mesa.players) == 0:ofim=True
        # Dá as cartas aos jogadores e ao dealer
        if ofim == False:
            for i in list(range(1,3)):
                for player in mesa.players:
                    # Dá uma carta ao jogador
                    player.hand[0].getCard(True)
                    # print (player.name + ' recebeu uma carta.')
                # Dá uma carta ao dealer
                dealopened = False
                if i == 1: dealopened = True
                mesa.dealer.hand[0].getCard(dealopened)
                # print ('Dealer '+ mesa.dealer.name + ' recebeu uma carta.')
            # page()
            # Para cada jogador:
            for player in mesa.players:
                # Para cada mão do jogador:
                for idx, phand in enumerate(player.hand):
                    print("\n")
                    willloop=True
                    while willloop == True:
                        dontpage=False
                        willloop = False
                        # printa mesa
                        zz.cls()
                        print (mesa.get(player,idx))
                        # avalia o score da mesa
                        # print ("Best "+str(phand.best()))
                        if phand.best() >0 and phand.best() < 21:
                            # Opções: (c)all, (r)aise, (p)ass, [(s)plit], (q)uit game
                            splitstr=''
                            splitopt='capt'
                            if phand[0].face == phand[1].face:
                                splitstr='(s)plitar | '
                                splitopt+='s'
                            question = "[ (c)hamar | (a)umentar | (p)assar | "+splitstr+"(t)erminar o jogo ]"
                            opt = zz.ask(question,splitopt)
                            # (s)plit:
                            if opt == "s":
                                player.splitHand(idx)
                                a = player.debt(mesa.pingo, False, len(player.hand)-1)
                                print (player.name + " splitou, pingou novamente ($"+str(a)+") e recebeu cartas novas em cada mão.")
                                willloop=True
                            # (r)aise:
                            if opt == "a":
                                # input amount
                                val=zz.getInt("Aumentar: $")
                                player.debt(val,False,idx)
                                if player.playing == True:
                                    dontpage=True
                                    willloop=True
                                else:
                                    if len(mesa.players) == 0: ofim=True
                            # (c)all:
                            if opt == "c":
                                # Recebe nova carta aberta, e loopa
                                phand.getCard(True)
                                willloop=True
                            # (p)ass:
                            if opt == "p":
                                # Faz nada, não. Segue para próxima mão.
                                dontpage=True
                            # (q)uit:
                            if opt == "t":
                                # Sai do jogo
                                ofim = True
                        elif phand.best() == 21:
                            print ("Black Jack!")
                        elif phand.blew() == True:
                            print ("Estourou!")
                    if dontpage==False:
                        page()
                    else:
                        zz.cls()

            if ofim == False:
                # Para a mão do dealer:
                dealer_finishes=False
                while dealer_finishes == False:
                    print (mesa.get_dealer())

                    win_chance = mesa.dealer_chances()
                    safe_chance = mesa.dealer_safe()
                    blow_chance = mesa.dealer_chances_toblow()
                    dealer_win_rate = mesa.dealer_winrate()

                    # print("Dealer's Winning Chance: "+str(win_chance))
                    # print("Dealer's Safe Chance: "+str(safe_chance))
                    # print("Dealer's Blow Chance: "+str(blow_chance))
                    # print("Dealer Winnning on Table: "+str(dealer_win_rate))
                    # print("Dealer's Greed: "+str(dealer_greed))

                    # Para se estourar
                    if mesa.dealer.hand[0].blew() == True:
                        print(dealer_name+" estourou.")
                        dealer_finishes=True

                    # Passa caso já ganhou de todos
                    elif dealer_win_rate == 1:
                        print(dealer_name+" passou.")
                        dealer_finishes=True

                    # Passa se já tiver Black Jack
                    elif mesa.dealer.hand[0].best_string() == "Black Jack":
                        print(dealer_name+" passou.")
                        dealer_finishes=True

                    # Recebe se não houver perigo
                    elif safe_chance >= 1:
                        print(dealer_name+" chamou.")
                        mesa.dealer.hand[0].getCard(True)

                    # Recebe se achar que deve
                    else:
                        dealer_think = mesa.dealer_think()
                        print(dealer_name+" "+dealer_think+".")
                        if dealer_think == "chamou":mesa.dealer.hand[0].getCard(True)
                        if dealer_think == "passou":dealer_finishes=True

                    page()

                # Calcula vencedores
                print (mesa.get_results())
                # Devolve o prêmio
                if mesa.passvalues() == "theend":ofim=True

                if ofim==False:
                    # Eleva o pingo
                    mesa.pingo+=pingo_inicial
                    print("\nO pingo agora é: $"+str(mesa.pingo)+".")
                    # Reseta hands
                    for player in mesa.players:player.hand=[Hand()]
                    mesa.dealer.hand=[Hand()]
                # Volta ao início

        if len(mesa.players) == 0:ofim=True
        page()

    print("\n\n\n           Obrigado por jogar! ;)\n\n\n")
    page()
    exit()


BlackJack()
