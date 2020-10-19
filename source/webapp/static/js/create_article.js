async function addArticle(event) {
    event.preventDefault();
    let response = await makeRequest(BASE_API_URL + 'article/create/', 'POST', {
        title: document.getElementById('id_title').value,
        text: document.getElementById('id_text').value
    });
    let data = await response.json();
    window.location.href = `${BASE_URL}article/${data.id}/`;
}

window.addEventListener('load', function () {
    const form = document.forms['article_create_form'];
    form.onsubmit = addArticle;
});