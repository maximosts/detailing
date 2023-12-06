# comments/views.py

from django.shortcuts import get_object_or_404, render, redirect
from .models import Comment
from .forms import CommentForm

def post_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('home')  # Redirect to the page where the comment was posted
    else:
        form = CommentForm()
    return render(request, 'comments/post_comment.html', {'form': form})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user is the author of the comment
    if request.user == comment.author:
        comment.delete()

    return redirect('home')

