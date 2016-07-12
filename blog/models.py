from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	slug = models.SlugField(max_length=200, blank=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def get_absolute_url(self):
		return reverse('blog.views.post_detail', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

def artigo_pre_save(signal, instance, sender, **kwargs):
	instance.slug = slugify(instance.title)

signals.pre_save.connect(artigo_pre_save, sender=Post)