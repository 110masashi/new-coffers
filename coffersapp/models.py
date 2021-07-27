from django.db import models

# Create your models here.
CATEGORY = (('coffee','コーヒー'),('arrange','コーヒーアレンジ'),('other','その他'))
EQUIPMENT = (('Hand','ハンドドリップ'),('Machine','マキネッタ'),('French','フレンチプレス'),('Aero','エアロプレス'),('Siphon','サイフォン式'),('Watered','水出し'),('other','その他'))
STAGE = (('弱い','1'),('少し弱い','2'),('丁度よい','3'),('少し強い','4'),('強い','5'))
ROAST =(('light','浅煎りマイルド'),('cinnamon','浅煎りストロング'),('medium','中煎りマイルド'),('high','中煎りストロング'),('city','中深煎りマイルド'),('Fullcity','中深煎りストロング'),('french','深煎りマイルド'),('italian','深煎りストロング'))

class BlogModel(models.Model):
    postdate = models.DateField(auto_now_add=True)
    equipment = models.CharField(
        max_length = 100,
        choices = EQUIPMENT
    )
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    roast = models.CharField(
        max_length = 10,
        choices = ROAST
    )
    bitter = models.CharField(
        max_length = 10,
        choices = STAGE
    )
    acidity = models.CharField(
        max_length = 10,
        choices = STAGE
    )
    rich = models.CharField(
        max_length = 10,
        choices = STAGE
    )
    aroma = models.CharField(
        max_length = 10,
        choices = STAGE
    )
    Beans_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
