% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}</h2>
<h3>Add New Release</h3>
<form action="/news" method="post">
    <p><input type="text" name="Author" pattern="[A-Za-z]{2,}"
    placeholder="Author name or nickname" required></p>
    <p><textarea name="Description" placeholder="Release description" required></textarea></p>
    <p><input 
    type="date" 
    name="Date" 
    placeholder="Release date" 
    required></p>
    <p><input type="submit" class="btn btn-new" value="Add Release"></p>
</form>
<br>
% show_modal = show_modal if 'show_modal' in locals() else False
% if show_modal:
  <dialog id="modal" open>
    <p>Invalid date! Please use YYYY-MM-DD format.</p>
    <form method="dialog">
      <button>OK</button>
    </form>
  </dialog>
% end
<br>
<h3>Latest Releases</h3>
<div class="news-container">
    % if news:
        % for item in news:
            <div class="news-card">
                <h4>Release #{{ item['id'] }}</h4>
                <p><strong>Author:</strong> {{ item['author'] }}</p>
                <p><strong>Description:</strong> {{ item['description'] }}</p>
                <p><strong>Release date:</strong> {{ item['date'] }}</p>
                <p class="news-date">Added: {{ item['added_date'] }}</p>
            </div>
        % end
    % else:
        <p>No releases yet. Be the first to add one!</p>
    % end
</div>