from django.shortcuts import render , redirect , get_object_or_404 , reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from blog.models import Post , Category , Comments
from blog.form import PostModelForm

from user.models import Freelancer , AllUser




# Create your views here.

# HOME PAGE DEF
def home_view(request):
    
    # #SEARCH BOX
    # keyword = request.GET["keyword"]
    # if keyword:
    #     categories =Post.objects.filter(title__contains = keyword)
        



    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    
    categories = Category.objects.filter(is_active = True)
    freelancers = Freelancer.objects.all()
    context = dict(
        posts = posts,
        categories = categories,
        latest_freelancer_list =freelancers,
        # keyword = keyword
        
    )
    

   

    return render(request,'home_page/index.html',context)


# SEARCH VİEW
def search_view(request):
    if request.method=='POST':
        keyword = request.POST['keyword']
        
        posts = Post.objects.filter(title__contains=keyword)
        context=dict(
            keyword = keyword,
            posts = posts
        )
        return render(request,'layouts/search.html',context)
    else:
        return render(request,'layouts/search.html',)
    



# POST DETAİL VİEW
def post_detail(request,id):
    # post = Post.objects.filter( id = id).first()
    post = get_object_or_404(Post,id=id)
    comments = post.comments.all()
    context = dict(
        post = post,
        comments = comments
    )
    return render(request,'layouts/detail.html',context)

# CATEGORY DEF
# def category_view(request,category_slug):
#     keyword = request.GET.get('keyword')
#     if keyword:

#     category = get_object_or_404(Category,slug = category_slug)
#     categories = Category.objects.filter(is_active = True).order_by('title')
#     posts = Post.objects.filter(
#         category = category,
#         is_active = True,
#     ).order_by('-created_at')
#     context = dict(
#         category = category,
#         categories = categories,
#         posts = posts 
#     )

#     return render(request,'home_page/index.html',context)

# PAGE DEF
def ceviri_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )
    return render(request,'layouts/ceviri.html',context)

def grafik_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )  
    return render(request,'layouts/grafik.html',context)


def muzik_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )   
    return render(request,'layouts/muzik.html',context)


def reklam_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )  
    
    

    return render(request,'layouts/reklam.html',context)


def video_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )  
    

    return render(request,'layouts/video.html',context)


def yazilim_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )  
    
    

    return render(request,'layouts/yazilim.html',context)



def yonetim_view(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)

    
    context =dict(
        posts = posts,
        categories = categories,
        
        
    )  
    

    return render(request,'layouts/yonetim.html',context)
    
    
    context =dict(
        
        
    )
    return render(request,'layouts/yonetim.html',context)

# COMMENT DEF
def addComment(request,id):
    post = get_object_or_404(Post,id = id)

    if request.method == "POST":
        comment_author = request.POST["comment_author"]
        comment_content = request.POST["comment_content"]

        newComment = Comments(comments_author = comment_author,comment_content = comment_content)
        newComment.posts = post
        newComment.save()
    return redirect(reverse("blog:post_detail",kwargs={"id":id}))
    # return redirect("/blog/blogdetail/"+ str(id))    



# def addBlog_view(request):
#     form = PostModelForm
#     context ={
#         'form':form
#      }
#     return render(request,'layouts/addblog.html',context)


# FREELANCER PAGES

def  freelancer_detail(request,freelancer_id):  
    freelancer_detail = Freelancer.objects.filter(pk=freelancer_id)
    context = dict(
        freelancer_detail = freelancer_detail
    )
    return render(request, "freelancer_temp/fre_for_user.html",context)

# def freelancer_detail(request, freelancer_id):
#     freelancer = get_object_or_404(Freelancer, pk=freelancer_id)
#     return render(request, "freelancer_temp/fre_for_user.html", {"freelancer": freelancer})


def freelancer_profil_duzenle(request):
    context = {

    }
    return render(request,'freelancer_temp/fre_profil_duzenle.html')

def freelancer_is(request):
    
    context = dict(
        
    )
        
    
    return render(request,'freelancer_temp/freelancer_is.html',context)

# POST YÜKLEME
@login_required(login_url='user:login_view')
def freelancer_post_card(request):
    form = PostModelForm()
    context = dict(
        form = form
    )
    if request.method == 'POST':
        form = PostModelForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            f = form.save(commit=False)
            f.free_user = request.user
            f.save()
            messages.success(request,'Postunuz Kaydedilmiştir')
    return render(request,'freelancer_temp/freelancer_post_card.html',context)





def freelancer_post(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.filter(is_active = True)
    freelancers = Freelancer.objects.all()
    

    
    context =dict(
        posts = posts,
        categories = categories,
    
        
        
    )  
    
    return render(request,'freelancer_temp/freelancer_post.html',context)


def freelancer_profil(request):
    context = {

    }
    return render(request,'freelancer_temp/freelancer_profil.html')


# USER PAGES



def user_profil(request):
    context = {
        
    }
    return render(request,'user_temp/user.html')

def user_profil_duzenle(request):
    context = {

    }
    return render(request,'user_temp/user_profil_duzenle.html')
