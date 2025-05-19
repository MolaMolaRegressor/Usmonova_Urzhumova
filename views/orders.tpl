% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>Create New Order</h3>
<form action="/orders" method="post">
    <p><input type="text" name="Name" pattern="[A-Za-z]{2,}"
    placeholder="Your name" required></p>
    <p><textarea name="Details" placeholder="Order Details"></textarea></p>
    <p><input
    type="numbers"
    name="Phone"
    placeholder="8 (___) ___-__-__"
    required></p>
    <p><input type="submit" class="btn btn-new" value="Place Order" ></p>
</form>
<br>
% if show_modal:
  <dialog id="modal" open>
    <p>Wrong phone, try again!</p>
    <form method="dialog">
      <button>OK</button>
    </form>
  </dialog>
% end
<br>
<h3>Existing Orders</h3>
<div class="orders-container">
    % if orders:
        % for order in orders:
            <div class="order-card">
                <h4>Order #{{ order['id'] }}</h4>
                <p><strong>Orderer:</strong> {{ order['name'] }}</p>
                % if order['description']:
                    <p><strong>Details:</strong> {{ order['description'] }}</p>
                % end
                <p><strong>Phone:</strong> {{ order['phone'] }}</p>
                <p class="order-date">Placed on: {{ order['date'] }}</p>
            </div>
        % end
    % else:
        <p>No orders yet. Be the first to place one!</p>
    % end
</div>
