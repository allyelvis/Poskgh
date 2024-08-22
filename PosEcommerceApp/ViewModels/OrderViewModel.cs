public class OrderViewModel
{
    public List<OrderItemViewModel> OrderItems { get; set; } = new List<OrderItemViewModel>();
}

public class OrderItemViewModel
{
    public int ProductId { get; set; }
    public int Quantity { get; set; }
    public decimal Price { get; set; }
}
