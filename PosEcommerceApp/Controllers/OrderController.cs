using Microsoft.AspNetCore.Mvc;
using System.Linq;

public class OrderController : Controller
{
    private readonly ApplicationDbContext _context;
    private readonly ExternalService _externalService;

    public OrderController(ApplicationDbContext context, ExternalService externalService)
    {
        _context = context;
        _externalService = externalService;
    }

    public IActionResult Create()
    {
        var products = _context.Products.ToList();
        ViewBag.Products = products;
        return View();
    }

    [HttpPost]
    public IActionResult Create(OrderViewModel model)
    {
        if (ModelState.IsValid)
        {
            var order = new Order
            {
                OrderDate = DateTime.Now,
                TotalAmount = model.OrderItems.Sum(item => item.Price * item.Quantity),
                OrderItems = model.OrderItems.Select(item => new OrderItem
                {
                    ProductId = item.ProductId,
                    Quantity = item.Quantity,
                    Price = item.Price
                }).ToList()
            };

            _context.Orders.Add(order);
            _context.SaveChanges();

            _externalService.ProcessPayment(order.TotalAmount); // Payment processing

            return RedirectToAction("Index");
        }

        return View(model);
    }
}
