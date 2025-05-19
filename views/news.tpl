% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}</h2>
<h3>Добавить новинку</h3>
<form action="/news" method="post">
    <p><input type="text" name="Author" pattern="[A-Za-zА-Яа-я]{2,}"
    placeholder="Имя автора или никнейм" required></p>
    <p><textarea name="Description" placeholder="Описание новинки" required></textarea></p>
    <p><input 
    type="date" 
    name="Date" 
    placeholder="Дата публикации" 
    required></p>
    <p><input type="submit" class="btn btn-new" value="Добавить новинку"></p>
</form>
<br>
% if show_modal:
  <dialog id="modal" open>
    <p>Некорректная дата! Используйте формат ГГГГ-ММ-ДД.</p>
    <form method="dialog">
      <button>OK</button>
    </form>
  </dialog>
% end
<br>
<h3>Последние новинки</h3>
<div class="news-container">
    % if news:
        % for item in news:
            <div class="news-card">
                <h4>Новинка #{{ item['id'] }}</h4>
                <p><strong>Автор:</strong> {{ item['author'] }}</p>
                <p><strong>Описание:</strong> {{ item['description'] }}</p>
                <p><strong>Дата публикации:</strong> {{ item['date'] }}</p>
                <p class="news-date">Добавлено: {{ item['added_date'] }}</p>
            </div>
        % end
    % else:
        <p>Пока нет новинок. Будьте первым!</p>
    % end
</div>
