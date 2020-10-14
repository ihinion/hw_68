async function onLike(event) {
    event.preventDefault();
    let likeBtn = event.target
    let url = likeBtn.href;

    try {
        let response = await makeRequest(url, 'POST');
        let data = await response.text();
        console.log(data);
        const counter = likeBtn.parentElement.getElementsByClassName('counter')[0];
        counter.innerText = data;
    }
    catch (error) {
        console.log(error)
    }

    likeBtn.classList.add('hidden');
    const unlikeBtn = likeBtn.parentElement.getElementsByClassName('unlike')[0];
    unlikeBtn.classList.remove('hidden');
}


async function onUnlike(event) {
    event.preventDefault();
    let unLikeBtn = event.target;
    let url = unLikeBtn.href;

    try {
        let response = await makeRequest(url, 'DELETE');
        let data = await response.text();
        console.log(data);
        const counter = unLikeBtn.parentElement
            .getElementsByClassName('counter')[0];
        counter.innerText = data;
    }
    catch (error) {
        console.log(error);
    }

    unLikeBtn.classList.add('hidden');
    const likeBtn = unLikeBtn.parentElement
        .getElementsByClassName('like')[0];
    likeBtn.classList.remove('hidden');
}

window.addEventListener('load', function () {
    const likeButtons = document.getElementsByClassName('like');
    const unlikeButtons = document.getElementsByClassName('unlike');
    for (let btn of likeButtons) {btn.onclick = onLike}
    for (let btn of unlikeButtons) {btn.onclick = onUnlike}
});