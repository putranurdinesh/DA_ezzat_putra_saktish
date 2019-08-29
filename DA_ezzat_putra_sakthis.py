import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Int Monthly Visitor.xlsx")

del df[' Brunei Darussalam ']
del df[' Indonesia ']
del df[' Malaysia ']
del df[' Philippines ']
del df[' Thailand ']
del df[' Viet Nam ']
del df[' Myanmar ']
del df[' Japan ']
del df[' Hong Kong ']
del df[' China ']
del df[' Taiwan ']
del df[' Korea, Republic Of ']
del df[' India ']
del df[' Pakistan ']
del df[' Sri Lanka ']
del df[' Saudi Arabia ']
del df[' Kuwait ']
del df[' UAE ']
del df[' United Kingdom ']
del df[' Germany ']
del df[' France ']
del df[' Italy ']
del df[' Netherlands ']
del df[' Greece ']
del df[' Belgium & Luxembourg ']
del df[' Switzerland ']
del df[' Austria ']
del df[' Scandinavia ']
del df[' CIS & Eastern Europe ']

df = df.drop(
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
     31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
     60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88,
     89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
     114, 115, 118, 119, 116, 117, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465,
     466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428,
     429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 389, 390,
     391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413,
     414, 415, 416, 417, 418, 359, 360,
     361, 362, 363, 364, 365, 366, 367, 368, 369, 370,
     371, 372, 373, 374, 375, 376, 377, 378, 379, 380,
     381, 382, 383, 384, 385, 386, 387, 388, 329, 330,
     331, 332, 333, 334, 335, 336, 337, 338, 339, 340
        , 341, 342, 343, 344, 345, 346, 347, 348, 349, 350
        , 351, 352, 353, 354, 355, 356, 357, 358, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310,
     311, 312, 313, 314, 315, 316, 317, 318, 319, 320,
     321, 322, 323, 324, 325, 326, 327, 328, 269, 270,
     271, 272, 273, 274, 275, 276, 277, 278, 279, 280,
     281, 282, 283, 284, 285, 286, 287, 288, 289, 290,
     291, 292, 293, 294, 295, 296, 297, 298, 240,
     241, 242, 243, 244, 245, 246, 247, 248, 249, 250,
     251, 252, 253, 254, 255, 256, 257, 258, 259, 260,
     261, 262, 263, 264, 265, 266, 267, 268])

df1 = df.head(12).sum()
df2 = df.loc[132:143].sum()
df3 = df.loc[144:155].sum()
df4 = df.loc[156:167].sum()
df6 = df.loc[180:191].sum()
df7 = df.loc[192:203].sum()
df8 = df.loc[204:215].sum()
df9 = df.loc[216:227].sum()
df10 = df.tail(12).sum()

new_df = {"Years": ['1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997'],
          " USA ": [226766, 247979, 261444, 253748, 287572, 307387, 343678, 345512, 374004, 376413],
          " Canada ": [42645, 55244, 61141, 58541, 63909, 63911, 65498, 61869, 65574, 62527],
          " Australia ": [361493, 450218, 456560, 367956, 385077, 365125, 347362, 346763, 351593, 381462],
          " New Zealand ": [79083, 86664, 72713, 61986, 61967, 62958, 69051, 66197, 67721, 70372],
          " Africa ": [46586, 54952, 56197, 55726, 69686, 97628, 100692, 86931, 79616, 70617]}

df = pd.DataFrame(new_df)
df.index = df["Years"]
del df["Years"]

des = df.describe()


class DA():
    def Usa(self):
        plt.plot(df.index, df[" USA "], label='USA')
        plt.legend(loc="best")
        plt.xlabel("Years")
        plt.ylabel("Amount of Visitors")
        plt.title("International Monthly Visitors(USA)")
        plt.grid()
        plt.show()
        # plt.savefig("USA.png")

    def Canada(self):
        plt.plot(df.index, df[" Canada "], label='CANADA')
        plt.legend(loc="best")
        plt.xlabel("Years")
        plt.ylabel("Amount of Visitors")
        plt.title("International Monthly Visitors(CANADA)")
        plt.grid()
        plt.show()
        # plt.savefig("CANADA.png")

    def Australia(self):
        plt.plot(df.index, df[" Australia "], label='Australia')
        plt.legend(loc="best")
        plt.xlabel("Years")
        plt.ylabel("Amount of Visitors")
        plt.title("International Monthly Visitors(Australia)")
        plt.grid()
        plt.show()
        # plt.savefig("AUSTRALIA.png")

    def New_Zealand(self):
        plt.plot(df.index, df[" New Zealand "], label='New Zealand')
        plt.legend(loc="best")
        plt.xlabel("Years")
        plt.ylabel("Amount of Visitors")
        plt.title("International Monthly Visitors(New Zealand)")
        plt.grid()
        plt.show()
        # plt.savefig("NEW ZEALAND.png")

    def Africa(self):
        plt.plot(df.index, df[" Africa "], label='Africa')
        plt.legend(loc="best")
        plt.xlabel("Years")
        plt.ylabel("Amount of Visitors")
        plt.title("International Monthly Visitors(Africa)")
        plt.grid()
        plt.show()
        # plt.savefig("AFRICA.png")

    def all(self):
        ax1 = df.plot(kind='bar', title="International Monthly Visitor(ALL)", figsize=(15, 15), legend=True,
                      fontsize=15,
                      grid=True)
        my_fig = ax1.get_figure()
        my_fig.savefig('International Monthly Visitor ALL')

    def avg(self):
        ax2 = des.plot(kind='bar', title="International Monthly Visitor(ALL AVG)", figsize=(15, 15), legend=True,
                       fontsize=15,
                       grid=True)
        my_fig = ax2.get_figure()
        my_fig.savefig('International Monthly Visitor ALL(AVG)')


ALLDF = DA()

print(df)
