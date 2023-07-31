import tkinter as tk
from tkinter import messagebox
import openai

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

class BlogPostGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blog-A-Lator")
        self.topic_label = tk.Label(root, text="Topic for blog post:")
        self.topic_label.pack()
        self.topic_entry = tk.Entry(root)
        self.topic_entry.pack()

        self.num_bullet_points_label = tk.Label(root, text="Number of bullet points you would like for blog post /"
                                                           "outline:")
        self.num_bullet_points_label.pack()
        self.num_bullet_points_entry = tk.Entry(root)
        self.num_bullet_points_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.generate_blog_post)
        self.submit_button.pack()

        self.generated_blog_post = None

    def generate_blog_post(self):
        topic = self.topic_entry.get()
        num_bullet_points = self.num_bullet_points_entry.get()

        # Format the prompt for the first interaction
        prompt = f"Provide a blog post outline for the topic of {topic} that has {num_bullet_points} bullet points."

        # Get the response from ChatGPT
        self.generated_blog_post = self.get_chatgpt_response(prompt)

        if self.generated_blog_post:
            self.show_bullet_points_dropdown()

    def get_chatgpt_response(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=150,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return None

    def show_bullet_points_dropdown(self):
        bullet_points = self.generated_blog_post.split("\n")

        self.bullet_point_label = tk.Label(root, text="Select a bullet point to expand upon:")
        self.bullet_point_label.pack()

        self.selected_bullet_point = tk.StringVar(root)
        self.selected_bullet_point.set(bullet_points[0])
        self.bullet_point_dropdown = tk.OptionMenu(root, self.selected_bullet_point, *bullet_points)
        self.bullet_point_dropdown.pack()

        self.expand_button = tk.Button(root, text="Expand", command=self.expand_bullet_point)
        self.expand_button.pack()

    def expand_bullet_point(self):
        selected_bullet_point = self.selected_bullet_point.get()

        # Format the prompt for the second interaction
        prompt = f"Expand upon {selected_bullet_point} bullet point from the previous answer with a full written post including citations."

        # Get the response from ChatGPT
        expanded_post = self.get_chatgpt_response(prompt)

        if expanded_post:
            self.show_expanded_post(expanded_post)

    def show_expanded_post(self, expanded_post):
        self.expanded_post_label = tk.Label(root, text="Expanded Post:")
        self.expanded_post_label.pack()

        self.expanded_post_text = tk.Text(root, wrap=tk.WORD)
        self.expanded_post_text.insert(tk.END, expanded_post)
        self.expanded_post_text.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlogPostGeneratorApp(root)
    root.mainloop()
