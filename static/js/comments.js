document.addEventListener('DOMContentLoaded', function () {
    // DELETE functionality
    const deleteButtons = document.querySelectorAll('.btn-delete');
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
    const deleteConfirm = document.getElementById('deleteConfirm');

    deleteButtons.forEach(button => {
        button.addEventListener('click', () => {
            const commentId = button.getAttribute('comment_id');
            const postSlug = window.location.pathname.split('/')[1];
            const deleteUrl = `/${postSlug}/delete_comment/${commentId}/`;

            deleteConfirm.setAttribute('href', deleteUrl);
            deleteModal.show();
        });
    });

    // EDIT functionality
    const editButtons = document.querySelectorAll('.btn-edit');
    const commentForm = document.getElementById('commentForm');
    const commentInput = commentForm.querySelector('textarea');
    const submitButton = document.getElementById('submitButton');

    editButtons.forEach(button => {
        button.addEventListener('click', () => {
            const commentId = button.getAttribute('comment_id');
            const commentText = document.getElementById(`comment${commentId}`).innerText.trim();
            const postSlug = window.location.pathname.split('/')[1];

            commentInput.value = commentText;
            submitButton.innerText = "Update";
            commentForm.setAttribute("action", `/${postSlug}/edit_comment/${commentId}/`);
        });
    });
});
