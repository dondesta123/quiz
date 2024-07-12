



from PyQt5 import*

from PyQt5.QtWidgets import*

from random import randint, shuffle


class pertanyaan():
    def __init__(self, text_quest, jwbn_bener, opt1, opt2, opt3):
        self.text.quest = text_quest
        self.jwbn_bener = jwbn_bener
        self.opt1 = opt1
        self.opt2 = opt2
        self.opt3 = opt3

app = QApplication([])


text_pertanyaan = Qlabel("siapa presiden pertama Republik Indonesia")


btn = QPushButton("Cek cuyy")


panel_quest = QGroupBox("pilihan ganda:")


btn1 = QRadioButton("opt 1")
btn2 = QRadioButton("opt 2")
btn3 = QRadioButton("opt 3")
btn4 = QRadioButton("opt 4")


btn_pil_ganda = QButtonGroup()
btn_pil_ganda.addButton(btn1)
btn_pil_ganda.addButton(btn2)
btn_pil_ganda.addButton(btn3)
btn_pil_ganda.addButton(btn4)


layout_utama_pil_ganda = QHBoxLayout()
layout_pil_ganda1 = QVBoxLayout()
layout_pil_ganda2 = QVBoxLayout()


layout_pil_ganda1.addWidget(btn1)
layout_pil_ganda1.addWidget(btn2)

layout_pil_ganda2.addWidget(btn3)
layout_pil_ganda2.addWidget(btn4)


layout_utama_pil_ganda.addLayout(layout_utama_pil_ganda1)
layout_utama_pil_ganda.addLayout(layout_utama_pil_ganda2)


panel_pil_ganda.setLayout(layout_utama_pil_ganda)


ansgroupbox = QGroupBox("Hasil Jawaban:")
lb_hasil = QLabel("Betul gak yaa????")
lb_jawaban = QLabel("Jawaban adalah jeng jeng jeng")

layout_res = QVBoxLayout()
layout_re.addWidget(lb_hasil, alignment=Qt.AlignLeft|Qt.alignTop)
layout_res.addWidget(ib_jawaban, alignment=Qt.AlignCenter)


ansgroupbox.setLayout(layout_res)


layout_quest = QHBoxLayout()
layout_pil_ganda_jawab = QHBoxLayout()
layout_btn = QHBoxLayout()


layout_quest.addWidget(text_pertanyaan, alignment=Qt.AlignCenter)
layout_pil_ganda_jawab.addWidget(panel_pil_ganda)
layout_pil_ganda_jawab.addWidget(ansgroupbox)
ansgroupbox.hide()

layout_btn.addWidget(3)
layout_btn.addWidget(btn,stretch=2)
layout_btn.addStretch(1)


layout_utama = QHBoxLayout()
layout_utama.addWidget(layout_quest,stretch=2)
layout_utama.addWidget(layout_pil_ganda_jawab,stretch=2)
layout_utama.addStretch(1)
layout_utama.addWidget(layout_btn,stretch=3)
layout_utama.addStretch(1)
layout_utama.setSpacing(5)


def show_result():

    panel_pil_ganda.hide()

    ansgroupbox.show()

    btn.setText("tengkyu, next")

def show_quest():

    panel_pil_ganda.show()

    ansgroupbox.hide()

    btn.setText("cek cuyy")



    btn_pil_ganda.setExclusive(False)

    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)

    btn_pil_ganda.setExclusive(True)

list_btn = [btn1,btn2,btn3,btn4]



def ask(q: pertanyaan)

    shuffle(list_btn)
    
    list_btn[0].setText(q.jwbn_bener)

    list_btn[1]setText(q.opt1)
    list_btn[2]setText(q.opt2)
    list_btn[3]setText(q.opt3)

    text_pertanyaan.setText(q.text_quest)

    ib Jawaban.setText(q.jwbn_bener)

    show_quest()


    def show_correct(hasil):
        lb_hasil.setText(hasil)
        show_result()
    
