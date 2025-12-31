# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts/step-3-add-the-checkout-script.md

# Step 3: Add the Checkout Script

{% hint style="danger" %}
You must be using Shopify Plus to integrate with Intelligems using the Checkout Script. Please see our [Functions Integration guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions) if this does not apply to you.
{% endhint %}

{% hint style="info" %}
The Intelligems checkout script will not apply any discounts or make other changes to orders until a price test is live. If you already use a Checkout Script, you can add ours to the same one to keep that functionality.
{% endhint %}

Adding our Checkout Script enables us to dynamically discount the price in the cart so that your customers pay exactly the price they see in other spots on the website. Follow the below steps to add the Intelligems Line Items Checkout Script to your Scripts Editor.

1. Install the Shopify Script editor [here](https://apps.shopify.com/script-editor).
2. If you already have a Line Items script, you can create a copy and edit it. Make sure our script runs first so that discounts get applied in the correct order. If you do not already have a Line Items script, create a new one.
3. Paste the loop below into the script. Save and publish the script.

```ruby
class Intelligems
  def initialize(discount_property = '_igp', allow_free = false)
    @volume_discount_property = '_igvd'
    @volume_discount_message_property = '_igvd_message'
    @deprecated_property = '_igLineItemDiscount'
    @discount_property = discount_property
    @allow_free = allow_free
  end

  def discount_product(line_item)
    ig_price = Money.new(cents: line_item.properties[@discount_property])

    discount = line_item.line_price - (ig_price * line_item.quantity)
    if discount > Money.zero
      if @allow_free or discount < line_item.line_price
        line_item.change_line_price(line_item.line_price - discount, message: 'Discount')
      end
   end
  end

def deprecated_discount_product(line_item)
  discount = Money.new(cents: line_item.properties[@deprecated_property])
    discount *= line_item.quantity

    if @allow_free or discount < line_item.line_price
      line_item.change_line_price(line_item.line_price - discount, message: 'Intelligems')
    end
  end

  def volume_discount(line_item)
    discount = Money.new(cents: line_item.properties[@volume_discount_property])
    discount *= line_item.quantity

    if discount < line_item.line_price
      message = line_item.properties[@volume_discount_message_property]
      line_item.change_line_price(line_item.line_price - discount, message: message)
    end
  end

  def run(cart)
    cart.line_items.each do |line_item|
      if !line_item.properties[@discount_property].nil? && !line_item.properties[@discount_property].empty?
        discount_product(line_item)
    elsif !line_item.properties[@volume_discount_property].nil? && !line_item.properties[@volume_discount_property].empty?
        volume_discount(line_item)
    elsif !line_item.properties[@deprecated_property].nil? && !line_item.properties[@deprecated_property].empty?
            deprecated_discount_product(line_item)
      end
    end
  end
end

intelligems = Intelligems.new()
intelligems.run(Input.cart)

Output.cart = Input.cart
```
