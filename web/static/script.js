function like(post_id) {
    const likeCount = document.getElementById(`likes-count-${post_id}`);
    const likeButton = document.getElementById(`like-button-${post_id}`);

    fetch(`/like-post/${post_id}`, {
        method: "POST",
    })
    .then((res) => res.json())
    .then((data) => {
        likeCount.innerHTML = data.likes;

        if (data.liked) {
            likeButton.classList.remove("far");
            likeButton.classList.add("fas");
        } else {
            likeButton.classList.remove("fas");
            likeButton.classList.add("far");
        }
    });
}