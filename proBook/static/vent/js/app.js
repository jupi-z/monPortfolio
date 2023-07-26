// Afficher le message de chargement
function showLoading() {
    document.querySelector('.loading').style.display = 'block';
}

// Cacher le message de chargement
function hideLoading() {
    document.querySelector('.loading').style.display = 'none';
}

// Afficher le message de succès
function showSuccess() {
    document.querySelector('.sent-message').style.display = 'block';
}

// Cacher le message de succès
function hideSuccess() {
    document.querySelector('.sent-message').style.display = 'none';
}

// Afficher le message d'erreur
function showError(error) {
    document.querySelector('.error-message').textContent = error;
    document.querySelector('.error-message').style.display = 'block';
}

// Cacher le message d'erreur
function hideError() {
    document.querySelector('.error-message').style.display = 'none';
}