from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ItemForm
from .models import Item


class ItemErrorFlashView(CreateView):
    """エラーがあるときにフラッシュメッセージを表示するView"""
    model = Item
    form_class = ItemForm
    
    def get_success_url(self):
        return reverse('my:item-detail', args=(self.object.id,))
        
    def form_invalid(self, form):
        if form.has_error('name'):
            # Modelのnameフィールドにエラーがある場合、フラッシュメッセージを表示
            messages.error(self.request, '!!ERROR!!')

        return super(ItemErrorFlashView, self).form_invalid(form)


class ItemFlashRemoveView(CreateView):
    """クエリ文字列がある場合、フラッシュメッセージを削除するView"""
    model = Item
    form_class = ItemForm
    
    def get_success_url(self):
        return reverse('my:item-detail', args=(self.object.id,))
        
    def form_valid(self, form):
        messages.success(self.request, 'Success (Remove ver.)')
        
        if self.request.META['QUERY_STRING'] == '':
            # クエリ文字列がない場合は、フラッシュメッセージを削除する
            # イテレータを回すことでフラッシュメッセージが削除されるので、
            # list()の他、forやリスト内包表記などでも可
            list(messages.get_messages(self.request))
    
        return super(ItemFlashRemoveView, self).form_valid(form)


class ItemFlashReuseView(CreateView):
    """一度削除してしまったフラッシュメッセージを再利用するView"""
    model = Item
    form_class = ItemForm
    
    def get_success_url(self):
        return reverse('my:item-detail', args=(self.object.id,))
        
    def form_valid(self, form):
        messages.success(self.request, 'Success (Reuse ver.)')
        
        # print()するときにイテレータを回してしまうけど、
        # フラッシュメッセージとしても表示したい場合
        msgs = messages.get_messages(self.request)
        for m in msgs:
            print(m)
        msgs.used = False
    
        return super(ItemFlashReuseView, self).form_valid(form)


class ItemFlashMixinView(SuccessMessageMixin, CreateView):
    """SuccessMessageMixinを使うView"""
    model = Item
    form_class = ItemForm
    
    # `%(field_name)s`という表記で、ModelであるItemのnameフィールドにある値を指す
    success_message = "%(name)s was created successfully"
    
    def get_success_url(self):
        return reverse('my:item-detail', args=(self.object.id,))
        
    def form_valid(self, form):
        # form_validではsuccess_messageで設定したフラッシュメッセージを削除できない
        list(messages.get_messages(self.request))
    
        return super(ItemFlashMixinView, self).form_valid(form)
