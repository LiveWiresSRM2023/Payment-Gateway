import "./Home.css"
import axios from "axios";
import { useState } from "react";
import useRazorpay from "react-razorpay";


export const Home = ()=>{

    const Razorpay = useRazorpay();
    const [amount, setAmount] = useState(500);
  
    // complete order
    const complete_order = (paymentID, orderID, signature)=>{
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/razorpay/order/complete/',
            data: {
                "payment_id": paymentID,
                "order_id": orderID,
                "signature": signature,
                "amount": amount
            }
        })
        .then((response)=>{
            console.log(response.data);
        })
        .catch((error)=>{
            console.log(error.response.data);
        })
    }

    const razorPay = ()=>{
        //create order
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/razorpay/order/create/',
            data: {
                amount: amount,
                currency: "INR"
            }
        })
        .then((response)=>{
            
            // get order id
            var order_id = response.data.data.id
            
            // handle payment
            const options = {
                key: process.env.REACT_APP_RAZORPAY_KEY_ID, // Enter the Key ID generated from the Dashboard
                name: "Acme Corp",
                description: "Test Transaction",
                image: "https://example.com/your_logo",
                order_id: order_id, //This is a sample Order ID. Pass the `id` obtained in the response of createOrder().
                handler: function (response) {

                    //complete order
                    complete_order(
                        response.razorpay_payment_id,
                        response.razorpay_order_id,
                        response.razorpay_signature
                    )
                },
                prefill: {
                name: "ABCDE",
                email: "youremail@example.com",
                contact: "9999999999",
                },
                notes: {
                address: "Razorpay Corporate Office",
                },
                theme: {
                color: "#3399cc",
                },
            };

            const rzp1 = new Razorpay(options);
            rzp1.on("payment.failed", function (response) {
                alert(response.error.code);
                alert(response.error.description);
                alert(response.error.source);
                alert(response.error.step);
                alert(response.error.reason);
                alert(response.error.metadata.order_id);
                alert(response.error.metadata.payment_id);
            });
            rzp1.open();
        })
        .catch((error)=>{
            console.log(error);
        })
    }

    return(
<div>
      <div className="logo">
        <img src="./LW1 (light).png" alt="Logo" />
      </div>
      <div className="container">
        <div className="image-section">
          <img src="./icon.png" alt="Placeholder Image" />
        </div>
        <div className="content-section">
          <h2>Event Name</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vel arcu at nulla semper efficitur.</p>
          <button type="button" onClick={razorPay}>Pay Now</button>
        </div>
      </div>
    </div>
    )
}
