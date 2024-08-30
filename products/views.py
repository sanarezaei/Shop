from django.views.generic import DetailView, ListView, CreateView
from .models import Product, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, reverse


class ProductListView(ListView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
     
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['product_id'] = self.object.id
        # logger.debug(context)
        # print('______Template context:______', context)
        return context
    
    # def product_detail(request, product_id):
    #     product = get_object_or_404(Product, id=product_id)
    #     return render(request, 'product_detail.html', {'product':product})




class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm


    def success_url(self):
        return reverse('product_list')
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, id=product_id)
        # if request.method == 'POST':
        #     form = CommentForm(request.POST)
        #     if form.is_valid():
        #         comment = form.save(commit=False)
        #         comment.product = product
        #         comment.save()
        #         return redirect('product_detail', product_id=product_id)
        #     else:
        #         form = CommentForm()
        #     return render(request, 'comment_create.html', {'form':form, 'product':product})
        
        
        obj.product = product
        
        return super().form_valid(form)
        
    def comment_create(request, product_id):
        product = get_object_or_404(Product, id=product_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.save()
                return redirect('product_detail', product_id=product_id)
        else:
            form = CommentForm()
        return render(request, 'comment_create.html', {'form': form, 'product': product})
        
