"use strict";

console.log('Test'); // Create Django Ajax Call

$("#addStock").submit(function () {
  var sizeInput = $('input[name="size"]').val().trim();
  var brandInput = $('input[name="brand"]').val().trim();
  var priceInput = $('input[name="price"]').val().trim();

  if (sizeInput && brandInput && priceInput) {
    // Create Ajax Call
    $.ajax({
      url: "{% url 'crud_ajax_create' %}",
      data: {
        'size': sizeInput,
        'brand': brandInput,
        'price': priceInput
      },
      dataType: 'json',
      success: function success(data) {
        if (data.user) {
          appendToUsrTable(data.user);
        }
      }
    });
  } else {
    alert("All fields must have a valid value.");
  }

  $('form#addStock').trigger("reset");
  return false;
}); // function appendToUsrTable(stock) {
//   $("#book-table > tbody:last-child").append(
//         <tr id="stock-${stock.id}">
//             <td class="stockSize" name="size">${stock.size}</td>
//             '<td class="stockBrand" name="brand">${stock.brand}</td>
//             '<td class="stockPrice" name="price">${stock.price}</td>
//             '<td align="center">
//                 <button class="btn btn-success form-control" onClick="editUser(${stock.id})" data-toggle="modal" data-target="#myModal">EDIT</button>
//             </td>
//             <td align="center">
//                 <button class="btn btn-danger form-control" onClick="deleteUser(${stock.id})">DELETE</button>
//             </td>
//         </tr>
//     );
// }
//# sourceMappingURL=crud.dev.js.map
