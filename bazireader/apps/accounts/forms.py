from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import bz_langit, bz_bumi

GENDER = [
    ('male', 'male'),
    ('female', 'female'),
]
DAY = [
    ('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5'), ('6','6'), ('7','7'), ('8','8'),
    ('9','9'), ('10','10'), ('11','11'), ('12','12'), ('13','13'), ('14','14'), ('15','15'),
    ('16','16'), ('17','17'), ('18','18'), ('19','19'), ('20','20'), ('21','21'), ('22','22'),
    ('23','23'), ('24','24'), ('25','25'), ('26','26'), ('27','27'), ('28','28'), ('29','29'),
    ('30','30'), ('31','31'),
]

MONTH = [
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
]

YEAR = [
    ('1940','1940'), ('1941','1941'), ('1942','1942'), ('1943','1943'), ('1944','1944'),
    ('1945','1945'), ('1946','1946'), ('1947','1947'), ('1948','1948'), ('1949','1949'),
    ('1950','1950'), ('1951','1951'), ('1952','1952'), ('1953','1953'), ('1954','1954'),
    ('1955','1955'), ('1956','1956'), ('1957','1957'), ('1958','1958'), ('1959','1959'),
    ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'),
    ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'),
    ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'),
    ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'),
    ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'),
    ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'),
    ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'),
    ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'),
    ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'),
    ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'),
    ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'),
    ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'),
    ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'),
    ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'),
]

HOUR = [
    ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
    ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'),
    ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'),
    ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'),
]

MIN = [('0', '0'), ('15', '15'), ('30','30'), ('45','45'),
]

ZONE = [(1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

]

LANGIT = [
    ('Jia', 'Jia甲'), ('Yi', 'Yi乙'), ('Bing', 'Bing丙'), ('Ding', 'Ding丁'), ('Wu', 'Wu戊'),
    ('Ji', 'Ji己'), ('Geng', 'Geng庚'), ('Xin', 'Xin辛'), ('Ren', 'Ren壬'), ('Gui', 'Gui癸')
]

BUMI = [
    ('Zi', 'Zi子'), ('Chou', 'Chou丑'), ('Yin', 'Yin寅'), ('Mao', 'Mao卯'), ('Chen', 'Chen辰'),
    ('Si', 'Si巳'), ('Uu', 'Wu午'), ('Wei', 'Wei未'), ('Shen', 'Shen申'), ('You', 'You酉'),
    ('Xu', 'Xu戌'), ('Hai', 'Hai亥'),
]

class bz_Form(forms.Form):
    #langit = bz_langit.objects.values('karakter').distinct()

    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "name"}))
    gender = forms.ChoiceField(required=True, label=_('gender'), choices=GENDER)

    day = forms.ChoiceField(required=True, label=_('day'), choices=DAY)

    month = forms.ChoiceField(required=True, label=_('month'), choices=MONTH)

    year = forms.ChoiceField(required=True, label=_('year'), choices=YEAR)

    hour = forms.ChoiceField(required=True, label=_('hour'), choices=HOUR)

    min = forms.ChoiceField(required=True, label=_('min'), choices=MIN)

    notime = forms.BooleanField(required=False, label=_("notime"))

    zone = forms.ChoiceField(required=True, label=_('zone'), choices=ZONE)

    #hhb = forms.ChoiceField(required=True, label=_('hhb'), choices=LANGIT)

    hha = forms.ChoiceField(required=True, label=_('hha'), choices=LANGIT)
    dda = forms.ChoiceField(required=True, label=_('dda'), choices=LANGIT)
    mma = forms.ChoiceField(required=True, label=_('mma'), choices=LANGIT)
    yya = forms.ChoiceField(required=True, label=_('yya'), choices=LANGIT)

    hhb = forms.ChoiceField(required=True, label=_('hhb'), choices=BUMI)
    ddb = forms.ChoiceField(required=True, label=_('ddb'), choices=BUMI)
    mmb = forms.ChoiceField(required=True, label=_('mmb'), choices=BUMI)
    yyb = forms.ChoiceField(required=True, label=_('yyb'), choices=BUMI)


    l2a = forms.ChoiceField(required=True, label=_('l2a'), choices=LANGIT)
    l1a = forms.ChoiceField(required=True, label=_('l2a'), choices=LANGIT)

    l2b = forms.ChoiceField(required=True, label=_('l2b'), choices=BUMI)
    l1b = forms.ChoiceField(required=True, label=_('l1b'), choices=BUMI)

