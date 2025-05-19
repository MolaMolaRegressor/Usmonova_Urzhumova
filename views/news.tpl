% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}</h2>
<h3>�������� �������</h3>
<form action="/news" method="post">
    <p><input type="text" name="Author" pattern="[A-Za-z�-��-�]{2,}"
    placeholder="��� ������ ��� �������" required></p>
    <p><textarea name="Description" placeholder="�������� �������" required></textarea></p>
    <p><input 
    type="date" 
    name="Date" 
    placeholder="���� ����������" 
    required></p>
    <p><input type="submit" class="btn btn-new" value="�������� �������"></p>
</form>
<br>
% if show_modal:
  <dialog id="modal" open>
    <p>������������ ����! ����������� ������ ����-��-��.</p>
    <form method="dialog">
      <button>OK</button>
    </form>
  </dialog>
% end
<br>
<h3>��������� �������</h3>
<div class="news-container">
    % if news:
        % for item in news:
            <div class="news-card">
                <h4>������� #{{ item['id'] }}</h4>
                <p><strong>�����:</strong> {{ item['author'] }}</p>
                <p><strong>��������:</strong> {{ item['description'] }}</p>
                <p><strong>���� ����������:</strong> {{ item['date'] }}</p>
                <p class="news-date">���������: {{ item['added_date'] }}</p>
            </div>
        % end
    % else:
        <p>���� ��� �������. ������ ������!</p>
    % end
</div>
