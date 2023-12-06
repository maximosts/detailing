from django.shortcuts import render, redirect  # Correct Django import

from comments.models import Comment
from comments.forms import CommentForm

def home(request):
    comments = Comment.objects.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # or any logic for assigning the author
            comment.save()
            return redirect('home')  # Redirect to refresh the page and see the new comment
    else:
        form = CommentForm()

    return render(request, 'main/home.html', {'comments': comments, 'form': form})
