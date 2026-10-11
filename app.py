from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
case_home = "API Preset TikTok Active!"
return case_home


@app.route("/search", methods=["GET"])
def search_preset():
  keyword = request.args.get("q", "")

  # Nanti bagian ini diisi logika/script untuk nyari video TikTok
  # Berdasarkan keyword yang diinput user.

  # Contoh data dummy (hasil tiruan sementara):
  dummy_results = [
      {
          "title": f"Preset AM Jedag Jedug - {keyword}",
          "video_url": "https://www.w3schools.com/html/mov_bbb.mp4",  # Contoh link video langsung putar
          "preset_link": "https://drive.google.com/contoh-preset",
      }
  ]

  return jsonify({"keyword": keyword, "results": dummy_results})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
