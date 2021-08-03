from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
import datetime

from .forms import bz_Form
from .models import bz_langit, bz_bumi, bz_story, bz_arti, bz_annual

def accounts(request: HttpRequest) -> HttpResponse:
    langit = bz_langit.objects.all()
    bumi = bz_bumi.objects.all()
    story = bz_story.objects.all()
    arti = bz_arti.objects.all()
    annual = bz_annual.objects.all()

    if request.method == "GET":
        form = bz_Form()
    elif request.method == "POST":
        form = bz_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            gender = form.cleaned_data["gender"]
            day = form.cleaned_data["day"]
            month = form.cleaned_data["month"]
            year = form.cleaned_data["year"]
            hour = form.cleaned_data["hour"]
            min = form.cleaned_data["min"]
            notime = form.cleaned_data["notime"]
            zone = form.cleaned_data["zone"]
            hha = form.cleaned_data['hha']
            dda = form.cleaned_data['dda']
            mma = form.cleaned_data['mma']
            yya = form.cleaned_data['yya']
            hhb = form.cleaned_data['hhb']
            ddb = form.cleaned_data['ddb']
            mmb = form.cleaned_data['mmb']
            yyb = form.cleaned_data['yyb']

            l2a = form.cleaned_data['l2a']
            l1a = form.cleaned_data['l1a']
            l2b = form.cleaned_data['l2b']
            l1b = form.cleaned_data['l1b']

            # put Natasha algorithm here

            ## cari elemen DM
            for item in langit.values('pinyin','elemen'):
                if item['pinyin'] == dda:
                    dm_elemen = item['elemen']

            ## 0. hitung jumlah elemen
            bz_kar = []
            bz_kar.append(hha)
            bz_kar.append(dda)
            bz_kar.append(mma)
            bz_kar.append(yya)
            bz_kar.append(hhb)
            bz_kar.append(ddb)
            bz_kar.append(mmb)
            bz_kar.append(yyb)

            bz_elm = []
            wood = ({"Jia", "Yi", "Yin", "Mao"})
            fire = ({"Bing", "Ding", "Si", "Uu"})
            metal = ({"Geng", "Xin", "Shen", "You"})
            water = ({"Ren", "Gui", "Hai", "Zi"})
            earth = ({"Wu", "Ji", "Chen", "Wei", "Xu", "Chou"})

            for kar in bz_kar:
                if kar in wood:
                    bz_elm.append("kayu")
                elif kar in fire:
                    bz_elm.append("api")
                elif kar in metal:
                    bz_elm.append("logam")
                elif kar in water:
                    bz_elm.append("air")
                elif kar in earth:
                    bz_elm.append("tanah")

            ## 1. kombo langit

            if "Jia" in bz_kar and "Ji" in bz_kar:
                bz_elm[bz_kar.index("Jia")] = "tanah"

            if "Yi" in bz_kar and "Geng" in bz_kar:
                bz_elm[bz_kar.index("Yi")] = "logam"

            if "Bing" in bz_kar and "Xin" in bz_kar:
                bz_elm[bz_kar.index("Xin")] = "air"
                bz_elm[bz_kar.index("Bing")] = "air"

            if "Ding" in bz_kar and "Ren" in bz_kar:
                bz_elm[bz_kar.index("Ding")] = "kayu"
                bz_elm[bz_kar.index("Ren")] = "kayu"

            if "Wu" in bz_kar and "Gui" in bz_kar:
                bz_elm[bz_kar.index("Gui")] = "api"
                bz_elm[bz_kar.index("Wu")] = "api"

            ## 2. transformasi

            if "Uu" in bz_kar and "Wei" in bz_kar:
                bz_elm[bz_kar.index("Wei")] = "api"

            if "Si" in bz_kar and "Shen" in bz_kar:
                bz_elm[bz_kar.index("Si")] = "air"
                bz_elm[bz_kar.index("Shen")] = "air"

            if "Chen" in bz_kar and "You" in bz_kar:
                bz_elm[bz_kar.index("Chen")] = "logam"

            if "Mao" in bz_kar and "Xu" in bz_kar:
                bz_elm[bz_kar.index("Mao")] = "api"
                bz_elm[bz_kar.index("Xu")] = "api"

            if "Yin" in bz_kar and "Hai" in bz_kar:
                bz_elm[bz_kar.index("Hai")] = "kayu"

            if "Chou" in bz_kar and "Zi" in bz_kar:
                bz_elm[bz_kar.index("Chou")] = "tanah"
                bz_elm[bz_kar.index("Zi")] = "tanah"

            ## 3. Combo bumi

            bz_karset = {bz_kar[0]}

            for v in range(1, 8):
                bz_karset.add(bz_kar[v])

            ar = 0
            l = 0
            k = 0
            ap = 0

            # element sets
            air = {"Zi", "Chen", "Shen"}
            logam = {"Chou", "Si", "You"}
            kayu = {"Mao", "Hai", "Wei"}
            api = {"Yin", "Uu", "Xu"}

            for w in air:
                if w in bz_karset:
                    ar = ar + 1

            for x in logam:
                if x in bz_karset:
                    l = l + 1

            for y in kayu:
                if y in bz_karset:
                    k = k + 1

            for z in api:
                if z in bz_karset:
                    ap = ap + 1

            if ar > 1:
                if "Chen" in bz_kar:
                    bz_elm[bz_kar.index("Chen")] = "air"
                if "Shen" in bz_kar:
                    bz_elm[bz_kar.index("Shen")] = "air"

            if l > 1:
                if "Chou" in bz_kar:
                    bz_elm[bz_kar.index("Chou")] = "logam"
                if "Si" in bz_kar:
                    bz_elm[bz_kar.index("Si")] = "logam"

            if k > 1:
                if "Hai" in bz_kar:
                    bz_elm[bz_kar.index("Hai")] = "kayu"
                if "Wei" in bz_kar:
                    bz_elm[bz_kar.index("Wei")] = "kayu"

            if ap > 1:
                if "Yin" in bz_kar:
                    bz_elm[bz_kar.index("Yin")] = "api"
                if "Xu" in bz_kar:
                    bz_elm[bz_kar.index("Xu")] = "api"

            ii = int(zone)
            age = [zone]
            for jj in range (1, 9):
                ii = 10 + ii
                age.append(str(ii))

            tahun = datetime.datetime.now().year
            umur = tahun - int(year)
            #print("umur:", umur)
            #print("age:", age)

            ## 4. Counting elemen

            kayu = 0
            api = 0
            tanah = 0
            logam = 0
            air = 0

            for elm in bz_elm:
                if elm == "kayu":
                    kayu = kayu + 1
                elif elm == "api":
                    api = api + 1
                elif elm == "tanah":
                    tanah = tanah + 1
                elif elm == "logam":
                    logam = logam + 1
                elif elm == "air":
                    air = air + 1

            #print("kayu", kayu)
            #print("api", api)
            #print("tanah", tanah)
            #print("logam", logam)
            #print("air", air)

            #5 - Tubuh Kuat/Lemah
            kek_tub = 0
            DM = bz_elm[1]
            #print ("DM", DM)

            #musim
            #heavenly stems
            wood_h = ({"Jia", "Yi"})
            fire_h = ({"Bing", "Ding"})
            metal_h = ({"Geng", "Xin"})
            water_h = ({"Ren", "Gui"})
            earth_h = ({"Wu", "Ji"})

            #earthly branches
            spring = ({"Yin", "Mao", "Chen"})
            summer = ({"Si", "Uu", "Wei"})
            autumn = ({"Shen","You", "Xu"})
            winter = ({"Hai", "Zi", "Chou"})

            if bz_kar[6] in spring:
                lahir = "musim semi"
            elif bz_kar[6] in summer:
                lahir = "musim panas"
            elif bz_kar[6] in autumn:
                lahir = "musim gugur"
            elif bz_kar[6] in winter:
                lahir = "musim dingin"
            else: lahir=""

            if bz_kar[1] in wood_h and (bz_kar[6] in spring or bz_kar[6] in winter):
                #print("Tubuh kuat secara musim.")
                kek_tub = kek_tub +2
            elif bz_kar[1] in fire_h and (bz_kar[6] in summer or bz_kar[6] in spring):
                #print("Tubuh kuat secara musim.")
                kek_tub = kek_tub +2
            elif bz_kar[1] in metal_h and (bz_kar[6] in autumn):
                #print("Tubuh kuat secara musim.")
                kek_tub = kek_tub +2
            elif bz_kar[1] in water_h and (bz_kar[6] in winter or bz_kar[6] in autumn):
                #print("Tubuh kuat secara musim.")
                kek_tub = kek_tub +2
            elif bz_kar[1] in earth_h and bz_kar[6] == "wei":
                #print("Tubuh kuat secara musim.")
                kek_tub = kek_tub +2
            elif bz_kar[1] in earth_h and bz_kar[6] in transitional:
                #print("Tubuh kuat secara musim.")
                kek_tub = kek_tub +1
            else:
                print("Tubuh kurang kuat secara musim.")
            #/musim

            #DM & Resource
            if DM == "kayu" and kayu > 1:
                #print("Tubuh kuat secara elemen DM.")
                kek_tub = kek_tub +1
                #print("friend", kayu-1)
                Resc = "air"
            elif DM == "api" and api > 1:
                #print("Tubuh kuat secara elemen DM.")
                kek_tub = kek_tub +1
                #print("friend", api-1)
                Resc = "kayu"
            elif DM == "tanah" and tanah > 1:
                #print("Tubuh kuat secara elemen DM.")
                kek_tub = kek_tub +1
                #print("friend", tanah-1)
                Resc = "api"
            elif DM == "logam" and logam > 1:
                #print("Tubuh kuat secara elemen DM.")
                kek_tub = kek_tub +1
                #print("friend", logam-1)
                Resc = "tanah"
            elif DM == "air" and air > 1:
                #print("Tubuh kuat secara elemen DM.")
                kek_tub = kek_tub +1
                #print("friend", air-1)
                Resc = "logam"
            else:
                if DM == "kayu":
                    #print("friend", 0)
                    Resc = "air"
                elif DM == "api":
                    #print("friend", 0)
                    Resc = "kayu"
                elif DM == "tanah":
                    #print("friend", 0)
                    Resc = "api"
                elif DM == "logam":
                    #print("friend", 0)
                    Resc = "tanah"
                elif DM == "air":
                    #print("friend", 0)
                    Resc = "logam"

            if Resc == "kayu":
                rescc = kayu
            elif Resc == "api":
                rescc = api
            elif Resc == "tanah":
                rescc = tanah
            elif Resc == "logam":
                rescc = logam
            elif Resc == "air":
                rescc = air

            if rescc >= 1:
                #print("Tubuh kuat secara resource.")
                kek_tub = kek_tub +1
            #print("Resource", Resc, rescc)

            #penilaian kekuatan tubuh
            #print("Score", kek_tub)

            if kek_tub >= 3:
                tubuh = "sangat kuat"
                tub = "kuat"

            elif kek_tub == 2:
                tubuh = "cukup kuat"
                tub = "kuat"

            elif kek_tub == 1:
                tubuh = "kurang kuat"
                tub = "kuat"

            else:
                tubuh =  "lemah"
                tub = "lemah"

            # 6. Cari Yongshen dan Xishen

            ## start with DM element, important!
            if DM == "kayu":
                tom = "kayu"
                tomc = kayu
            elif DM == "api":
                tom = "api"
                tomc = api
            elif DM == "tanah":
                tom = "tanah"
                tomc = tanah
            elif DM == "logam":
                tom = "logam"
                tomc = logam
            else:
                tom = "air"
                tomc = air

            ## continue with output, wealth, officer, resource
            if kayu>tomc:
                tom = "kayu"
                tomc = kayu
            if api>tomc:
                tom = "api"
                tomc = api
            if tanah>tomc:
                tom = "tanah"
                tomc = tanah
            if logam>tomc:
                tom = "logam"
                tomc = logam
            if air>tomc:
                tom = "air"
                tomc = air

            if DM == "kayu":
                if tom == "api": tomu = "output"
                if tom == "tanah": tomu = "wealth"
                if tom == "logam": tomu = "officer"
            elif DM == "api":
                if tom == "tanah": tomu = "output"
                if tom == "logam": tomu = "wealth"
                if tom == "air": tomu = "officer"
            elif DM == "tanah":
                if tom == "logam": tomu = "output"
                if tom == "air": tomu = "wealth"
                if tom == "kayu": tomu = "officer"
            elif DM == "logam":
                if tom == "air": tomu = "output"
                if tom == "kayu": tomu = "wealth"
                if tom == "api": tomu = "officer"
            elif DM == "air":
                if tom == "kayu": tomu = "output"
                if tom == "api": tomu = "wealth"
                if tom == "tanah": tomu = "officer"
            else:
                tomu = ""
            print(name, "DM", DM, "too much", tom, "/", tomu)

            for item in story.values('dm','tubuh','too_much','yongshen','story'):
                if item['dm'] == DM and item['tubuh'] == tub and item['too_much'] == tom:
                    YS = item['yongshen']
                    mystory = item['story']

            mystory = dm_elemen + " lahir di " + lahir + ". " + mystory

            #print("Yongshen", YS)
            YS_c = 0
            XS_c = 0
            # take these inputs from stories database (YS) and element assignment algorithm

            for elm in bz_elm:
                if elm == YS:
                    YS_c = YS_c + 1

            offc = {
                "kayu": "logam",
                "api": "air",
                "tanah": "kayu",
                "logam": "api",
                "air": "tanah"
            }

            melahirkan = {
                "kayu": "air",
                "api": "kayu",
                "tanah": "api",
                "logam": "tanah",
                "air": "logam"
            }

            menyerap = {
                "kayu": "api",
                "api": "tanah",
                "tanah": "logam",
                "logam": "air",
                "air": "kayu"
            }

            menyeimbangkan = {
                "kayu": "logam",
                "api": "air",
                "tanah": "kayu",
                "logam": "api",
                "air": "tanah"
            }

            if YS_c >= 2 and YS == offc[DM]:
                XS = menyeimbangkan[YS]
            elif YS_c == 0 or YS_c == 1:
                XS = melahirkan[YS]
            else:
                XS = menyerap[YS]

            for elmx in bz_elm:
                if elmx == XS:
                    XS_c = XS_c + 1

            #print("XiShen", XS, XS_c)

            if YS_c >= 1:
                YSn = "(Yong Shen nyata)"
            else:
                YSn = "(Yong Shen tidak nyata)"
            #print(YSn)

            if XS_c >= 1:
                XSn = "(Xi Shen nyata --> hoki)"
            else:
                XSn = "(Xi Shen tidak nyata --> harus cari hoki dari karir)"
            #print(XSn)

            # 7 - Maskulin vs. Feminin
            yang = ({"Jia", "Bing", "Wu", "Geng", "Ren", "Zi", "Yin", "Chen", "Uu", "Shen", "Xu"})
            yin = ({"Yi", "Ding", "Ji", "Xin", "Gui", "Chou", "Mao", "Si", "Wei", "You", "Hai"})

            yangc = 0
            yinc = 0

            for kar in bz_kar:
                if kar in yang:
                    yangc = yangc + 1
                elif kar in yin:
                    yinc = yinc + 1

            if yangc > 4:
                masfem = "Maskulin"
            elif yangc == 4:
                masfem = "Netral"
            else:
                masfem = "Feminin"

            if YS == "kayu":
                tulang = kayu
            elif YS == "api":
                tulang = api
            elif YS == "tanah":
                tulang = tanah
            elif YS == "logam":
                tulang = logam
            else:
                tulang = air

            if XS == "kayu":
                tulang = tulang + kayu
            elif XS == "api":
                tulang = tulang + api
            elif XS == "tanah":
                tulang = tulang + tanah
            elif XS == "logam":
                tulang = tulang + logam
            else:
                tulang = tulang + air

            if tulang >4:
                km = "kaya"
            else:
                km = "miskin"

            #diagram
            if DM == "air":
                output = "kayu"
                wealth = "api"
                officer = "tanah"
            if DM == "kayu":
                output = "api"
                wealth = "tanah"
                officer = "logam"
            if DM == "api":
                output = "tanah"
                wealth = "logam"
                officer = "air"
            if DM == "tanah":
                output = "logam"
                wealth = "air"
                officer = "kayu"
            if DM == "logam":
                output = "air"
                wealth = "kayu"
                officer = "api"

            # 8. pasangan, 9. karir, 10. kesehatan
            pasangan = bz_elm[5]

            karir_air = "Perlengkapan kamar mandi (ledeng, kran, bathtub, dll.), bisnis minuman (kedai minuman), perikanan, cafe, pelayaran dan perkapalan, aquarium/pembuatan kolam ikan, pabrik es, toko kristal, toko kaca, peralatan pancing, dokter spesialis kelamin dan THT, pelari, transportasi, toko/industri plastik, bahan-bahan kimia, redaktur"
            karir_kayu = "Tukang kayu, kontraktor, perusahaan pengangkutan atau pengiriman, perkebunan, tour & travel (pariwisata), guru, pendidik, toko kertas, toko buku, perpustakaan, persewaan buku, pabrik triplek atau kayu lapis, toko obat herbal, toko perabotan (furniture) dan perkakas, pewarna makanan, fitness center atau sentra kebugaran, alat musik klasik, kursus bela diri, olah ragawan, perdagangan, distribusi, operator telepon, dokter spesialis hati (liver)"
            karir_api = "Tukang las atau reparasi alat-alat listrik, periklanan, asuransi, pengecoran logam, fotografi dan studio foto, bisnis hiburan (entertainment), dokter spesialis jantung, toko serba ada (supermarket), restoran, katering, toko roti, toko alat-alat listrik, industri kain, industri film dan bioskop, programmer, penyanyi, pemain akrobat/sirkus, public relation"
            karir_tanah = "Batu-Batuan, toko/pabrik semen, pergudanagn pedagang kelontong, pertanian, hasil bumi, pekerja sosial, dokter spesialis kandungan, barang antik, bidang keagamaan (termasuk tempat ibadah), kasir, pemakaman dan layanan kematian, koperasi"
            karir_logam = "Industri peralatan besi, perbankan dan valuta asing, persenjataan, pabrik dengan mesin-mesin besar, tentara, polisi, satpam, dokter spesialis paru-paru dan gigi, toko besi, toko emas, sekolah hukum, hardware komputer, perhotelan dan tempat peristirahatan, bursa saham"

            if YS=="air": karir = karir_air
            if YS=="kayu": karir= karir_kayu
            if YS == "api": karir = karir_api
            if YS == "tanah": karir = karir_tanah
            if YS == "logam": karir = karir_logam

            health_air = "Banyak elemen air. Jaga ginjal dan kandung kemih, hati-hati gangguan saraf." \
                         "Hindari makanan asin, begadang dan alkohol. Tidak boleh kering. "
            health_kayu = "Banyak elemen kayu. Jaga hati dan pancreas, hati-hati kolesterol." \
                          "Hindari makan terlalu kenyang. Tidak boleh banyak angin. "
            health_api = "Banyak elemen api. Jaga jantung dan usus kecil, hati-hati darah tinggi." \
                         "Hindari makanan asin dan berlemak. Tidak boleh kepanasan. "
            health_tanah = "Banyak elemen tanah. Jaga lambung dan limpa, hati-hati maag." \
                           "Hindari makanan pedas dan asam. Tidak boleh kedinginan. "
            health_logam = "Banyak elemen logam. Jaga paru-paru, hati-hati sesak napas." \
                           "Hindari rokok, debu dan polusi. Tidak boleh kekeringan. "

            health = ""
            if kayu >= 3:
                health = health + health_kayu
            if api >= 3:
                health = health + health_api
            if tanah >= 3:
                health = health + health_tanah
            if logam >= 3:
                health = health + health_logam
            if air >= 3:
                health = health + health_air

            # 11. arti harm clash dll
            bz_karbumi = []
            meaning = ""
            for xx in bz_kar:
                for item in bumi.values('pinyin','karakter'):
                    if item['pinyin'] == xx:
                        bz_karbumi.append(item['karakter'])
            #print(bz_karbumi)

            for item in arti.values('first', 'second', 'mean', 'xing'):
                if item['first'] in bz_karbumi and item['second'] in bz_karbumi and item['xing'] ==0:
                    meaning = meaning + item['mean']+ ", "
                if item['xing'] ==1:
                    cnt = 0
                    for xx in bz_karbumi:
                        if xx == item['first']: cnt = cnt+1
                    if cnt >1:
                        meaning = meaning + item['mean'] + ","

            # 12. luck period
            lucka = [l1a,l2a]
            luckb = [l1b,l2b]
            pera = ['Jia','Yi','Bing','Ding','Wu','Ji','Geng','Xin','Ren','Gui']
            perb = ['Zi','Chou','Yin','Mao','Chen','Si','Uu','Wei','Shen','You','Xu','Hai']

            ii = pera.index(lucka[0])
            jj = pera.index(lucka[1])

            if ii < jj:
                for kk in range(1,8):
                    if (jj+kk) >=10:
                        lucka.append(pera[jj+kk-10])
                    else:
                        lucka.append(pera[jj+kk])
            elif ii > jj:
                for kk in range(1,8):
                    if (jj-kk) <0:
                        lucka.append(pera[jj-kk+10])
                    else:
                        lucka.append(pera[jj-kk])
            #print (lucka)

            ii = perb.index(luckb[0])
            jj = perb.index(luckb[1])

            if ii < jj:
                for kk in range(1, 8):
                    if (jj + kk) >= 12:
                        luckb.append(perb[jj + kk - 12])
                    else:
                        luckb.append(perb[jj + kk])
            elif ii > jj:
                for kk in range(1, 8):
                    if (jj - kk) < 0:
                        luckb.append(perb[jj - kk + 12])
                    else:
                        luckb.append(perb[jj - kk])
            #print(luckb)

            ## cari period bagus dan period jelek dari luckb
            lb_elm = []
            pp = []

            bwood = ({"Yin", "Mao", "Chen"})
            bfire = ({"Si", "Uu", "Wei"})
            bmetal = ({"Shen", "You", "Xu"})
            bwater = ({"Hai", "Zi", "Chou"})

            for lb in luckb:
                if lb in bwood:
                    lb_elm.append("kayu")
                elif lb in bfire:
                    lb_elm.append("api")
                elif lb in bmetal:
                    lb_elm.append("logam")
                elif lb in bwater:
                    lb_elm.append("air")

            #DM kuat sekali, elemen bagus: output, wealth, officer
            elm_bagus = {YS, XS}
            if DM == tom:
                elm_bagus.add(output)
                elm_bagus.add(wealth)
                elm_bagus.add(officer)

            if tub == "lemah":
                elm_bagus.add(DM)
                elm_bagus.add(Resc)

            if tub == "kuat" and tomu == "output":
                elm_bagus.add(wealth)
                elm_bagus.add(officer)

            if tub == "kuat" and tomu == "wealth":
                elm_bagus.add(output)
                elm_bagus.add(officer)

            if tub == "kuat" and tomu == "officer":
                elm_bagus.add(output)
                elm_bagus.add(wealth)

            print ("elemen bagus:", elm_bagus)

            for lbe in lb_elm:
                if lbe in elm_bagus:  # elemen2 bagus (bedasarkan YS dan diagram)
                    pp.append("bagus")
                else:
                    pp.append("kurang bagus")

            ## panjang umur periode-6

            p6 = ""
            if bz_kar[6] in ('Hai','Zi'): p6 = "api"
            elif bz_kar[6] in ('Yin','Mao'): p6 = "logam"
            elif bz_kar[6] in ('Si','Uu'): p6 = "air"
            elif bz_kar[6] in ('Shen','You'): p6 = "kayu"
            else: p6 = "tanah"

            if p6 in elm_bagus:
                #print ("meaning: ", meaning)
                meaning = "Potensi panjang umur. " + meaning

            else:
                ag = int(age[5])+5
                meaning = "Jaga kesehatan di sekitar usia " + str(ag) + ". " + meaning

            ## 13. annual luck

            tahuny = []
            tahuna = []
            tahunb = []
            tahunc = ["", "", "", "", "",""]

            for ii in range (0,5):
                tahuny.append(tahun+ii)

                for item in annual.values('year','first','second'):
                    if item['year'] == tahun+ii:
                        taha = item['first']
                        tahb = item['second']

                for item in langit.values('id', 'pinyin'):
                    if item['id'] == taha:
                        tahuna.append(item['pinyin'])

                for item in bumi.values('id', 'pinyin'):
                    if item['id'] == tahb:
                        tahunb.append(item['pinyin'])
                #print (tahuna, tahunb)

                tahunc[ii] = tahunc[ii] + ckilling(tahuna[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + clangit(tahuna[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + charm(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + clash(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + ctrans(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + chorse(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + cpeach(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + cgrave(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + cxing(tahunb[ii], bz_kar) + " "
                tahunc[ii] = tahunc[ii] + ckombi(tahunb[ii], bz_kar) + " "

                #print (tahuny[ii], tahunc[ii])



            return render(request, "accounts/result.html", {"name": name,
                                                            "gender": gender,
                                                            "day": day,
                                                            "month": month,
                                                            "year": year,
                                                            "hour": hour,
                                                            "min": min,
                                                            "notime": notime,
                                                            "zone": zone,
                                                            "age": age,
                                                            "umur": umur,
                                                            "lahir": lahir,
                                                            "dm_elemen": dm_elemen,
                                                            "bz_kar": bz_kar,
                                                            "bz_elm": bz_elm,
                                                            "kayu": kayu,
                                                            "api": api,
                                                            "tanah": tanah,
                                                            "logam": logam,
                                                            "air": air,
                                                            "tubuh": tubuh,
                                                            "masfem": masfem,
                                                            "YS": YS,
                                                            "XS": XS,
                                                            "YSn" : YSn,
                                                            "XSn" : XSn,
                                                            "mystory": mystory,
                                                            "Resc": Resc,
                                                            "output": output,
                                                            "wealth": wealth,
                                                            "officer": officer,
                                                            "km": km,
                                                            "pasangan": pasangan,
                                                            "karir": karir,
                                                            "health": health,
                                                            "lucka": lucka,
                                                            "luckb": luckb,
                                                            "meaning": meaning,
                                                            "pp": pp,
                                                            "tahuny": tahuny,
                                                            "tahuna": tahuna,
                                                            "tahunb": tahunb,
                                                            "tahunc": tahunc,
                                                            })

        else:
            return render(request, "accounts/accounts.html", {"form": form, "success": True})
    else:
        raise NotImplementedError

    return render(request, "accounts/accounts.html", {"form": form})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

def ckilling(tahuna, bz_kar):
    ss=""
    if tahuna == "Geng" and "Jia" in bz_kar:
        ss= "Geng merusak Jia."

    elif tahuna == "Xin" and "Yi" in bz_kar:
        ss= "Xin merusak Yi."

    elif tahuna == "Ren" and "Bing" in bz_kar:
        ss= "Ren merusak Bing."

    elif tahuna == "Gui" and "Ding" in bz_kar:
        ss= "Gui merusak Ding."

    elif tahuna == "Jia" and "Wu" in bz_kar:
        ss= "Jia merusak Wu."

    elif tahuna == "Yi" and "Ji" in bz_kar:
        ss= "Yi merusak Ji."

    elif tahuna == "Bing" and "Geng" in bz_kar:
        ss= "Bing merusak Geng."

    elif tahuna == "Ding" and "Xin" in bz_kar:
        ss= "Ding merusak Xin."

    elif tahuna == "Wu" and "Ren" in bz_kar:
        ss= "Wu merusak Ren."

    elif tahuna == "Ji" and "Gui" in bz_kar:
        ss= "Ji merusak Gui."


    return ss

def clangit(tahuna, bz_kar):
    ss=""
    if tahuna == "Jia" and "Ji" in bz_kar:
        ss= "Jia Ji berubah jadi tanah."

    elif tahuna == "Ji" and "Jia" in bz_kar:
        ss= "Jia Ji berubah jadi tanah."

    elif tahuna == "Geng" and "Yi" in bz_kar:
        ss= "Geng Yi berubah jadi logam."

    elif tahuna == "Yi" and "Geng" in bz_kar:
        ss= "Geng Yi berubah jadi logam."

    elif tahuna == "Bing" and "Xin" in bz_kar:
        ss= "Bing Xin berubah jadi air."

    elif tahuna == "Xin" and "Bing" in bz_kar:
        ss= "Bing Xin berubah jadi air."

    elif tahuna == "Ren" and "Ding" in bz_kar:
        ss= "Ren Ding berubah jadi kayu."

    elif tahuna == "Ding" and "Ren" in bz_kar:
        ss= "Ren Ding berubah jadi kayu."

    elif tahuna == "Wu" and "Gui" in bz_kar:
        ss= "Wu Gui berubah jadi air."

    elif tahuna == "Gui" and "Wu" in bz_kar:
        ss= "Wu Gui berubah jadi air."


    return ss

def charm(tahunb, bz_kar):
    ss=""
    if tahunb == "Si" and "Yin" in bz_kar:
        ss= "Hurts as 3rd party in accident when element is too strong."

    elif tahunb == "Yin" and "Si" in bz_kar:
        ss= "Hurts as 3rd party in accident when element is too strong."

    elif tahunb == "Chen" and "Mao" in bz_kar:
        ss= "Indicate lawsuit or legal offense."

    elif tahunb == "Mao" and "Chen" in bz_kar:
        ss= "Indicate lawsuit or legal offense."

    elif tahunb == "Uu" and "Chou" in bz_kar:
        ss= "Temperament, Lack patience, Denoted accident if unbalanced /element is too strong."
    elif tahunb == "Chou" and "Uu" in bz_kar:
        ss= "Temperament, Lack patience, Denoted accident if unbalanced /element is too strong."

    elif tahunb == "Wei" and "Zi" in bz_kar:
        ss= "Confusion Harm,  Problem bringing children."

    elif tahunb == "Zi" and "Wei" in bz_kar:
        ss= "Confusion Harm,  Problem bringing children."

    elif tahunb == "Shen" and "Hai" in bz_kar:
        ss= "Mental Harm, Attack through mind games."

    elif tahunb == "Hai" and "Shen" in bz_kar:
        ss= "Mental Harm, Attack through mind games."

    elif tahunb == "You" and "Xu" in bz_kar:
        ss= "Body Harm, Head, face, or back problem Surgery, Physical problem."

    elif tahunb == "Xu" and "You" in bz_kar:
        ss= "Body Harm, Head, face, or back problem Surgery, Physical problem."


    return ss

def clash(tahunb, bz_kar):
    ss=""
    if tahunb == "Zi" and "Uu" in bz_kar:
        ss= "Unease, Not peaceful, Mental and Passion clash."

    elif tahunb == "Uu" and "Zi" in bz_kar:
        ss= "Unease, Not peaceful, Mental and Passion clash."

    elif tahunb == "Hai" and "Si" in bz_kar:
        ss= "Nosy clash, Interfering with another business/affair, Offering help where help is not needed."

    elif tahunb == "Si" and "Hai" in bz_kar:
        ss= "Nosy clash, Interfering with another business/affair, Offering help where help is not needed."

    elif tahunb == "Wei" and "Chou" in bz_kar:
        ss= "Internal Problem,  Self Problem, Pindah Kerja/Rumah."

    elif tahunb == "Chou" and "Wei" in bz_kar:
        ss= "Internal Problem,  Self Problem, Pindah Kerja/Rumah."

    elif tahunb == "Yin" and "Shen" in bz_kar:
        ss= "Emotional clash, Accident."

    elif tahunb == "Shen" and "Yin" in bz_kar:
        ss= "Emotional clash, Accident."

    elif tahunb == "Mao" and "You" in bz_kar:
        ss= "Betrayal, Lost trust from relative or friend, Love betrayal."

    elif tahunb == "You" and "Mao" in bz_kar:
        ss= "Betrayal, Lost trust from relative or friend, Love betrayal."

    elif tahunb == "Chen" and "Xu" in bz_kar:
        ss= "Movement,  Counter relative /spouse,  Hurt children,  Reduce life span."

    elif tahunb == "Xu" and "Chen" in bz_kar:
        ss= "Movement,  Counter relative /spouse,  Hurt children,  Reduce life span."


    return ss

def ctrans(tahunb, bz_kar):
    ss=""
    if tahunb == "Si" and "Shen" in bz_kar:
        ss= "Si Shen bertransformasi jadi air."

    elif tahunb == "Shen" and "Si" in bz_kar:
        ss= "Si Shen bertransformasi jadi air."

    elif tahunb == "Uu" and "Wei" in bz_kar:
        ss= "Wu Wei bertransformasi jadi api."

    elif tahunb == "Wei" and "Uu" in bz_kar:
        ss= "Wu Wei bertransformasi jadi api."

    elif tahunb == "Chen" and "You" in bz_kar:
        ss= "Chen You bertransformasi jadi logam."

    elif tahunb == "You" and "Chen" in bz_kar:
        ss= "Chen You bertransformasi jadi logam."

    elif tahunb == "Mao" and "Xu" in bz_kar:
        ss= "Mao Xu bertransformasi jadi api."

    elif tahunb == "Xu" and "Mao" in bz_kar:
        ss= "Mao Xu bertransformasi jadi api."

    elif tahunb == "Hai" and "Yin" in bz_kar:
        ss= "Yin Hai bertransformasi jadi kayu."

    elif tahunb == "Yin" and "Hai" in bz_kar:
        ss= "Yin Hai bertransformasi jadi kayu."

    elif tahunb == "Zi" and "Chou" in bz_kar:
        ss= "Zi Chou bertransformasi jadi tanah."

    elif tahunb == "Chou" and "Zi" in bz_kar:
        ss= "Zi Chou bertransformasi jadi tanah."


    return ss

def chorse(tahunb, bz_kar):
    ss=""

    if ("Yin" in bz_kar or "Si" in bz_kar or "Shen" in bz_kar or "Hai" in bz_kar):

        if tahunb in ['Yin', 'Si', 'Shen', 'Hai']:
            ss= "Flying horse indicates movement / travel."

    return ss

def cpeach(tahunb, bz_kar):
    ss=""
    if ("Zi" in bz_kar or "Mao" in bz_kar or "Uu" in bz_kar or "Yao" in bz_kar):
        if tahunb in ("Zi", "Mao", "Uu", "Yao"):
            ss= "Peach blossom indicates changing jobs/home or bullying/harassment."

    return ss

def cgrave(tahunb, bz_kar):
    ss=""
    if ("Chou" in bz_kar or "Chen" in bz_kar or "Wei" in bz_kar or "Xu" in bz_kar):
        if tahunb in ("Chou", "Chen", "Wei", "Xu"):
            ss= "Grave indicates immediate danger."

    return ss

def cxing(tahunb, bz_kar):
    ss=""
    if "Chen" in bz_kar and tahunb == "Chen":
        ss= "Terlalu jaga image."

    elif "Uu" in bz_kar and tahunb == "Uu":
        ss= "Terlalu semangat, semua dilabrak."

    elif "You" in bz_kar and tahunb == "You":
        ss= "Terlalu sistematis, kesempatan hilang."

    elif "Hai" in bz_kar and tahunb == "Hai":
        ss= "Terlalu easy going, mudah percaya."

    return ss

def ckombi(tahunb, bz_kar):
    ss=""
    bb = bz_kar.copy()
    bb.append(tahunb)
    #print(bb)

    if "Hai" in bb and "Zi" in bb and "Chou" in bb:
        ss= "Kombinasi air sempurna menghancurkan api, menyerap logam."
    if "Yin" in bb and "Mao" in bb and "Chen" in bb:
        ss= "Kombinasi kayu sempurna menghancurkan tanah, menyerap air."
    if "Si" in bb and "Uu" in bb and "Wei" in bb:
        ss= "Kombinasi api sempurna menghancurkan logam, menyerap kayu."
    if "Shen" in bb and "You" in bb and "Xu" in bb:
        ss= "Kombinasi logam sempurna menghancurkan kayu, menyerap tanah."
    if "Chou" in bb and "Chen" in bb and "Wei" in bb and "Xu" in bb:
        ss= "Kombinasi tanah sempurna menghancurkan air, menyerap api."

    bb.remove(tahunb)
    return ss

