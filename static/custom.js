document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    searchInput.addEventListener('input', function() {
        const query = this.value.trim();

        if (query === '') {
            searchResults.innerHTML = '';
            return;
        }

        // Make AJAX request to fetch search results
        fetch(`/autocomplete?query=${query}`)
            .then(response => response.json())
            .then(data => {
                // Display search results
                let html = '';
                data.forEach(result => {
                    html += `<div class="autocomplete-item">${result.title} by ${result.author}</div>`;
                });
                searchResults.innerHTML = html;

                // Add event listeners to search result items
                const autocompleteItems = document.querySelectorAll('.autocomplete-item');
                autocompleteItems.forEach(item => {
                    item.addEventListener('click', function() {
                        searchInput.value = this.textContent;
                        searchResults.innerHTML = '';
                    });
                });
            })
            .catch(error => {
                console.error('Error fetching autocomplete results:', error);
                searchResults.innerHTML = '<div class="autocomplete-error">Error fetching results</div>';
            });
    });
});
