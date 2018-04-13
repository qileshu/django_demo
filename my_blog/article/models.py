from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100) # 博客题目
    date_time = models.DateTimeField(auto_now_add = True) # 博客日期
    content = models.TextField(blank = True, null = True) # 博客正文
    
    # 返回该对象的字符串形式，但这个方法只能有self这一个参数
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
